import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import Semaphore
from tqdm import tqdm
import pandas as pd


class Parallelizer:
    def __init__(self, executor_type="thread", max_workers=None, use_tqdm=False,
                 batch_size=None, rate_limit_time=None, concurrent_limit=None,
                 thread_worker_multiplier=2):
        self.executor_type = executor_type
        self.thread_worker_multiplier = thread_worker_multiplier
        self.max_workers = max_workers or self._default_workers(executor_type)
        self.use_tqdm = use_tqdm
        self.batch_size = batch_size
        self.rate_limit_time = rate_limit_time
        self.concurrent_limit = concurrent_limit

    def _default_workers(self, executor_type):
        if executor_type == "thread":
            return os.cpu_count() * self.thread_worker_multiplier
        elif executor_type == "process":
            return os.cpu_count()
        else:
            raise ValueError("executor_type must be 'thread' or 'process'.")

    @classmethod
    def _execute_with_limit(cls, fn, args, semaphore):
        with semaphore:
            return fn(args)

    def connate(self, fn, iterable, executor_type=None, max_workers=None, use_tqdm=None,
                batch_size=None, rate_limit_time=None, concurrent_limit=None,
                thread_worker_multiplier=None, print_interval=None):
        is_dataframe = isinstance(iterable, pd.DataFrame)
        if is_dataframe:
            iterable = iterable.to_dict(orient="records")
        elif isinstance(iterable, dict):
            iterable = [iterable]

        executor_type = executor_type or self.executor_type
        max_workers = max_workers or self.max_workers
        use_tqdm = use_tqdm if use_tqdm is not None else self.use_tqdm
        batch_size = batch_size or self.batch_size
        rate_limit_time = rate_limit_time or self.rate_limit_time
        concurrent_limit = concurrent_limit or self.concurrent_limit

        Executor = ThreadPoolExecutor if executor_type == "thread" else ProcessPoolExecutor
        results = []

        batches = [iterable[i:i + batch_size] for i in range(0, len(iterable), batch_size)] if batch_size else [iterable]

        for batch in batches:
            semaphore = Semaphore(concurrent_limit) if concurrent_limit else None

            with Executor(max_workers=max_workers) as executor:
                futures = executor.map(lambda x: self._execute_with_limit(fn, x, semaphore) if semaphore else fn, batch)
                results.extend(tqdm(futures, desc="Processing", total=len(batch)) if use_tqdm else futures)

        if is_dataframe:
            return pd.DataFrame(results)
        return results


_default_parallelizer = Parallelizer()


def connate(fn, iterable, **kwargs):
    return _default_parallelizer.connate(fn, iterable, **kwargs)
