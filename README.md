# Pygame Setup Guide

## Step 1: Clone the git repository into your local
```bash
git clone https://github.com/ErnestasTamosiunas/space_shooter.git
```

---

## Step 2: Create Virtual Environment
```bash
python3 -m venv venv
```

---

## Step 3: Activate Virtual Environment
### On Linux/Mac:
```bash
source venv/bin/activate
```

### On Windows (PowerShell):
```bash
.\venv\Scripts\Activate
```

### Example:
`(venv) user@machine project_dir $`

---

## Step 4: Create `requirements.txt` (if it doesn't exist)
```bash
echo "pygame==2.6.1" > requirements.txt
```

---

## Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Step 6: Verify Installation
```bash
python3 -m pygame
```

## Step 7: Run game
- While inside the root folder of this repository
```bash
python3 main.py
```

### Expected Output:
- The command will return an **error** with exit code `1` (expected), but it will confirm that `pygame` is installed.

---

## Notes
#### Always activate the virtual environment before running the game:
```bash
source venv/bin/activate
```

## To update `requirements.txt` after adding dependencies:
```bash
pip freeze > requirements.txt
```
