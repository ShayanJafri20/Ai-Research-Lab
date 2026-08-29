# NLP Research Track — V1.0 through V1.3, in Depth

Why this file exists: the roadmap's own checklist (in [[03-Roadmap]]) is meant to stay a light, scannable list — it can't hold the level of detail this track actually needs. The user is heading toward AI research and explicitly asked for the full treatment here: research papers, real mathematics and tensor dimensions, weight-training mechanics, and "why does this file exist" reasoning applied to ML code structure, not just web code. This file is the detailed plan that [[03-Roadmap]]'s checklist entry now points to, so nothing here has to be re-derived or re-promised in a future session. Referenced from [[00-Hub]].

## Governing principles for this whole track

- **One layer below the abstraction, no deeper** ([[01-Philosophy]] hard rule 7) — real math and tensor shapes, not "implement PyTorch from scratch."
- **Hand-rolled before framework** (hard rule 3/7) — every architecture gets built with plain Python/NumPy first, at the smallest scale that makes the concept concrete, *before* PyTorch is introduced. PyTorch's actual selling point (autograd, GPU acceleration) is only obvious once you've felt the pain of computing gradients by hand.
- **Depth even on things already known** (hard rule 1, and the 2026-08-20 decision in [[04-Decisions]]) — the user has PyTorch/ML background already; that changes pacing (faster refresher), not depth (still full math, still full implementation).
- **A real paper at each stage**, not a syllabus dumped up front — introduced when it's the actual answer to a problem just hit, matching how every tool in this whole project has been introduced.
- **Real data throughout** — the three Gutenberg texts already in `lab/datasets/` are the actual training data used from V1.0 onward, not synthetic toy text (the one exception: the XOR problem below, which is intentionally *not* text — it's a pure math warm-up before text enters the picture at all).

## Stage 0 (pre-V1.0) — Neural network foundations

**Where:** Learning Sandbox (see [[07-Sandbox-Log]]), not the main `lab/` app — this is a disposable exercise for a single confusing concept, not a feature of the AI Research Lab itself.

**Build:** a hand-written MLP (multi-layer perceptron), pure Python/NumPy, solving XOR.

**Why XOR specifically:** it's the smallest possible problem that a single-layer network *provably cannot solve* (Minsky & Papert, 1969, *Perceptrons*) — proving concretely why multiple layers plus non-linear activation functions are necessary at all, before ever touching a real dataset.

**Concepts covered:**
- Sigmoid and tanh activation functions — the math, and *why* non-linearity between layers is what makes stacking layers meaningful at all (without it, any number of layers collapses into one linear function).
- Forward pass — how a layer's output becomes the next layer's input; the actual matrix/vector shapes involved (dimensions of weights, inputs, outputs at each layer).
- Backpropagation — computing gradients by hand, layer by layer, using the chain rule. This is the actual "manual backprop pain" that later justifies PyTorch.
- Gradient descent — using those gradients to actually update weights, and why the learning rate matters.
- Loss function (likely mean squared error or binary cross-entropy for this toy case) — what "the network is wrong" actually means numerically.

**No PyTorch, no DataLoader here** — this is deliberately the smallest, most manual version of the whole idea.

## V1.0 — Tokenization + RNN

**Real data:** one (then all three) of the Gutenberg texts in `lab/datasets/`.

**Concepts:**
- Tokenization — splitting real text into a vocabulary and integer IDs. Models take numbers, never raw text.
- UNK tokens — what happens to a word not in the vocabulary.
- Padding/masking — once batching multiple real texts of different lengths together, why the model needs to be told which positions are "real" vs. padding.
- The RNN itself — hidden state, recurrence, *why* weights are shared across every time step (this is the direct extension of Stage 0's MLP: same forward-pass/backprop ideas, plus a loop over time).
- Real dimensions to track explicitly: vocabulary size, embedding dimension, hidden state size, sequence length, batch size — and how each one shows up as an actual tensor shape.

**Paper:** Elman (1990), *"Finding Structure in Time"* — the original simple RNN. Companion (not a formal paper, but excellent intuition): Andrej Karpathy, *"The Unreasonable Effectiveness of Recurrent Neural Networks."*

**Framework:** this is where **PyTorch and `DataLoader`** get introduced for real — once Stage 0's hand-rolled backprop has made clear what autograd is actually saving you from. Explain what `DataLoader` solves (batching, shuffling, iterating over a real dataset efficiently) before using it, same as every other tool in this project.

## V1.1 — LSTM / GRU

**Motivating problem:** the RNN from V1.0 will visibly struggle with longer sequences — it forgets earlier context. Concretely felt via real training on the Gutenberg texts, not just told about.

**Paper:** Hochreiter & Schmidhuber (1997), *"Long Short-Term Memory."*

**Concepts:** gating mechanisms (forget/input/output gates), why they solve the vanishing-gradient problem RNNs have, GRU as a simplified alternative.

## V1.2 — Attention

**Motivating problem:** even with LSTM/GRU, processing is still fundamentally sequential (one time step at a time) — a real bottleneck for longer sequences and parallelization.

**Paper:** Bahdanau et al. (2014), *"Neural Machine Translation by Jointly Learning to Align and Translate."*

**Concepts:** attention weights, query/key/value framing (introduced conceptually here, formalized fully at V1.3), why "looking at everything at once" solves the sequential bottleneck.

## V1.3 — Transformer + BPE

**Paper:** Vaswani et al. (2017), *"Attention Is All You Need."*

**Concepts:**
- BPE (byte-pair encoding) / subword tokenization — introduced here specifically because word-level tokenization's limits (vocabulary size, out-of-vocabulary words) become real at this scale.
- Self-attention, multi-head attention, positional encoding (since removing recurrence means the model has no inherent sense of word order otherwise).
- **"Why does this config file exist"** gets answered concretely here, for the first time on the ML side of the project (hard rule 9, applied to ML code, not just web code) — real Transformer training code typically separates config (hyperparameters) from model code from training-loop code, and this is where that separation actually earns its place, rather than being copied blindly from a tutorial.
- Train/validation split as genuine practice, not just a concept — ahead of full formalization at V1.4 (Experiment tracking), where this becomes systematic.

## After V1.3

V1.4 onward (Experiment tracking, Reinforcement Learning at V1.5, Redis/jobs/WebSockets, Model registry, Inference server, Distributed training) are already scoped in [[03-Roadmap]]'s main table and causal chain — this file's job ends at V1.3, the point where the "core NLP architectures" arc completes. No need to duplicate those later stages here.
