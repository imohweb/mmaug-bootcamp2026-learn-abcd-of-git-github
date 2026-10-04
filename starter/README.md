# AI sentiment workshop fixture

A tiny **word-based deterministic classifier**, not a real LLM or production AI service. It exists so beginners can practice Git, GitHub, tests and CI without credentials or cloud costs.

## Run locally

Use Python **3.12 or newer**. Create a venv:

```bash
python -m venv .venv
```

Activate with `source .venv/bin/activate` on macOS/Linux, `.venv\Scripts\Activate.ps1` in Windows PowerShell, or `.venv\Scripts\activate.bat` in Windows Command Prompt.

```bash
python -m pip install -r requirements.txt
python app.py "This is good"
python -m pytest -q
python -m evals.run_evaluation
```

Expected: `positive`, passing tests, and `Evaluation passed: 3/3`.

## Repository map

- `app.py`: validate input and classify recognized words.
- `prompts/system.txt`: example prompt artifact; the classifier does not call a model or execute this prompt.
- `tests/`: deterministic unit tests.
- `evals/`: three public synthetic examples and their evaluation runner.
- `requirements.txt`: pinned test dependency.
- `pytest.ini`: test path and import configuration.
- `.gitignore`: excluded environments, caches and credential files.

## Limits and safety

The app recognizes a few positive/negative words. It cannot understand context, negation, sarcasm or model-quality requirements. Blank input is rejected explicitly. Real AI systems need richer evaluations and appropriate responsible-use review.

No API key, private data or model weights are required. Never commit secrets, `.env`, private keys or a virtual environment.
