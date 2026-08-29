# NLP Research Track — V1.0 through V1.3, in Depth

Why this file exists: the roadmap's own checklist (in [[03-Roadmap]]) is meant to stay a light, scannable list — it can't hold the level of detail this track actually needs. The user is heading toward AI research and explicitly asked for the full treatment here: research papers, real mathematics and tensor dimensions, weight-training mechanics, and "why does this file exist" reasoning applied to ML code structure, not just web code. This file is the detailed plan that [[03-Roadmap]]'s checklist entry now points to, so nothing here has to be re-derived or re-promised in a future session. Referenced from [[00-Hub]].

## Governing principles for this whole track

- **One layer below the abstraction, no deeper** ([[01-Philosophy]] hard rule 7) — real math and tensor shapes, not "implement PyTorch from scratch."
- **Hand-rolled before framework** (hard rule 3/7) — every architecture gets built with plain Python/NumPy first, at the smallest scale that makes the concept concrete, *before* PyTorch is introduced. PyTorch's actual selling point (autograd, GPU acceleration) is only obvious once you've felt the pain of computing gradients by hand.
- **Depth even on things already known** (hard rule 1, and the 2026-08-20 decision in [[04-Decisions]]) — the user has PyTorch/ML background already; that changes pacing (faster refresher), not depth (still full math, still full implementation).
- **A real paper at each stage**, not a syllabus dumped up front — introduced when it's the actual answer to a problem just hit, matching how every tool in this whole project has been introduced.
- **"Implement the paper" is literal, added 2026-08-30:** each architecture's **forward pass** is built from its actual paper equations using low-level tensor ops (matrix multiplies, `sigmoid`/`tanh`, etc.) — never PyTorch's pre-built high-level classes for the architecture-of-focus (`nn.LSTM`, `nn.MultiheadAttention`, `nn.Transformer` are explicitly off-limits for *implementing* these; using them would skip the exact understanding this track exists to build). **Backward pass (gradients)** is the one place PyTorch's autograd genuinely takes over, starting at V1.0 — the sole exception is Stage 0's MLP, where backprop is derived fully by hand in NumPy, specifically so the pain autograd removes is actually felt once, before it starts happening automatically.
- **Real data throughout** — the three Gutenberg texts already in `lab/datasets/` are the actual training data used from V1.0 onward, not synthetic toy text (the one exception: the XOR problem below, which is intentionally *not* text — it's a pure math warm-up before text enters the picture at all).
- **How we actually work through each implementation, added 2026-08-30 (user explicitly asked how this collaboration should work):** (1) explain the relevant block of the paper in plain terms, connecting it to math already known; (2) describe the shape of the code needed — not the finished answer, pseudocode/structure; (3) the user attempts writing it, even if unsure — a wrong attempt is more useful than no attempt, since it shows exactly where the gap is; (4) check it, fix/complete what's needed, and explicitly connect the resulting code back to the specific paper equation it implements. For very small, single-formula pieces (e.g. `sigmoid`), a solo attempt first is reasonable; for a full architecture block (an LSTM cell, attention scores), default to the heavier walkthrough from the start. This is hard rule 6, applied specifically to paper-to-code translation — a real, separate skill from understanding the underlying math, expected to feel unfamiliar at first the same way writing the first HTML skeleton did.

## Optimizers (spans multiple stages, added 2026-08-30)

- **Plain gradient descent** — Stage 0, already the mechanism used to update the XOR MLP's weights.
- **Momentum** — a natural next question once plain gradient descent's slow/oscillating convergence is actually seen on real training (likely V1.0, once training on real Gutenberg text makes this concrete rather than abstract).
- **Adam** — the modern default optimizer almost everything actually uses in practice; worth implementing by hand once (moving averages of gradients and squared gradients, bias correction) given how universal it is, likely around V1.0-V1.1 once a real training loop exists to plug it into.
- **Muon** — a newer, more specialized optimizer; covered conceptually (what problem it solves relative to Adam) rather than necessarily reimplemented from scratch, unless it becomes directly relevant later — the reimplement-vs-understand line gets decided the same problem-first way as everything else in this project, not pre-committed here.

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
- Self-attention, multi-head attention, positional encoding (since removing recurrence means the model has no inherent sense of word order otherwise) — **sinusoidal** (the original Vaswani et al. 2017 method) first, then **RoPE** (Rotary Position Embedding — Su et al. 2021, *"RoFormer: Enhanced Transformer with Rotary Position Embedding"*) as the modern alternative used in more recent models (e.g. LLaMA-style), a good "why did practice move on from the original paper" comparison once sinusoidal is understood.
- **"Why does this config file exist"** gets answered concretely here, for the first time on the ML side of the project (hard rule 9, applied to ML code, not just web code) — real Transformer training code typically separates config (hyperparameters) from model code from training-loop code, and this is where that separation actually earns its place, rather than being copied blindly from a tutorial.
- Train/validation split as genuine practice, not just a concept — ahead of full formalization at V1.4 (Experiment tracking), where this becomes systematic.

## After V1.3

V1.4 onward (Experiment tracking, Reinforcement Learning at V1.5, Redis/jobs/WebSockets, Model registry, Inference server, Distributed training) are already scoped in [[03-Roadmap]]'s main table and causal chain — this file's job ends at V1.3, the point where the "core NLP architectures" arc completes. No need to duplicate those later stages here.
