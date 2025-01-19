# LoopAlle
LoopAlle is a Python package designed to simplify parallel processing for DataFrames, lists, and dictionaries. 
It supports thread-based and process-based execution, with additional features like batching, concurrency limits, 
and interval-based debugging.

## Folder structure 

```
parafor/
├── parafor/
│   ├── __init__.py
│   ├── parallelizer.py
├── tests/
│   ├── test_parallelizer.py
├── README.md
├── setup.py
├── pyproject.toml
├── LICENSE
├── MANIFEST.in

```

## Features

- Parallelize processing of DataFrames, lists, or dictionaries.
- Supports both threading and multiprocessing.
- Flexible configurations for batching, rate limiting, and concurrency control.
- Handles exceptions gracefully with full traceback.
- Designed for both small-scale and enterprise use cases.

## Installation

Install LoopAlle using pip:

```bash
pip install loopalle
```

### **Package Description**

**`loopalle`** is a Python library designed to simplify and optimize the parallelization of tasks, whether they involve **DataFrames**, **lists**, or **dictionaries**. The package is ideal for tasks where independent data processing is required, offering support for both threading and multiprocessing. 

It is highly configurable, enabling enterprise-grade scalability and flexibility with features like:
- **Batch Processing**
- **Concurrency Limits**
- **Thread and Process Control**
- **Rate Limiting**
- **Customizable Debugging**

---

### **Key Functions**

#### **1. `connate`**
The primary function of the package, **`connate`**, provides a simple interface to parallelize loops. It works seamlessly across various input types (DataFrames, lists, dictionaries) and ensures consistent output formats.

**Parameters**:
- `fn`: The function to be applied to each item.
- `iterable`: The data to process (DataFrame, list, or dictionary).
- `executor_type`: Execution type (`"thread"` or `"process"`, defaults to `"thread"`).
- `max_workers`: Maximum number of workers (default: system-determined based on CPU cores).
- `batch_size`: Number of items per batch (default: processes all at once).
- `concurrent_limit`: Limits the number of tasks executing simultaneously.
- `rate_limit_time`: Pause duration (in seconds) between batches.
- `print_interval`: Logs parameters and results for every nth index.

**Returns**:
- Processed results in the same format as the input:
  - **DataFrame in → DataFrame out**
  - **List in → List out**
  - **Dictionary in → List of dictionaries out**

---

#### **2. `Parallelizer`**
The **`Parallelizer`** class provides object-level configuration for tasks that require reusability or repetitive execution. Instead of passing parameters repeatedly, you can define default settings during initialization.

**Usage**:
```python
from loopalle import Parallelizer

# Create a reusable Parallelizer instance
parallelizer = Parallelizer(executor_type="process", batch_size=10, use_tqdm=True)

# Use it to process tasks
results = parallelizer.connate(fn, data)
```

---

### **When to Use `loopalle`**

#### **1. Data Processing**
- Use when working with large pandas DataFrames where row-wise operations are independent:
  - E.g., Applying a transformation function to each row.
```python
import pandas as pd
from loopalle import connate

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

def process_row(row):
    return {"A": row["A"] * 2, "B": row["B"] + 1}

result = connate(process_row, df)
print(result)
```

---

#### **2. API Calls**
- Ideal for making parallel API calls with optional **rate limiting** or **batching**.
```python
import requests
from loopalle import connate

urls = ["https://api.example.com/data1", "https://api.example.com/data2"]

def fetch_url(url):
    response = requests.get(url)
    return response.json()

results = connate(fetch_url, urls, executor_type="thread", rate_limit_time=1)
print(results)
```

---

#### **3. List or Dictionary Processing**
- Useful for batch-processing JSON-like objects or other dictionary-based data structures.
```python
data = [{"A": 1, "B": 4}, {"A": 2, "B": 5}, {"A": 3, "B": 6}]

def process_item(item):
    return {"A": item["A"] * 3, "B": item["B"] - 1}

results = connate(process_item, data)
print(results)
```

---

#### **4. Concurrency Limits**
- When you need to limit simultaneous executions for **I/O-bound tasks** (e.g., file reads/writes, web scraping):
```python
from loopalle import connate

file_paths = ["file1.txt", "file2.txt", "file3.txt"]

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

results = connate(read_file, file_paths, executor_type="thread", concurrent_limit=2)
print(results)
```

---

#### **5. Enterprise Applications**
- Perfect for scaling parallel workloads in large-scale applications, such as:
  - **ETL Pipelines**: Processing chunks of data in parallel.
  - **Machine Learning**: Parallel feature engineering or model inference.
  - **Real-Time Systems**: Handling independent tasks concurrently.

---

### **Why Use `loopalle`?**

1. **Ease of Use**: Abstracts the complexities of threading and multiprocessing with a clean API.
2. **Flexibility**: Works with various data formats (DataFrames, lists, dictionaries).
3. **Scalability**: Enterprise-grade performance with support for large-scale workloads.
4. **Robust Debugging**: Features like `print_interval` and error handling make debugging seamless.
5. **Customizable**: Fine-tune execution with batching, concurrency limits, and rate limiting.

---

connect with me @ manishks.bitsindri@gmail.com

