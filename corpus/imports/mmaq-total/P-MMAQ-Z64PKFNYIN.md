---
schema: qual/card@1
id: P-MMAQ-Z64PKFNYIN
kind: problem
title: (a) Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
relations: []
review: draft
solved: true
---

::: problem
(a) Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire
    function. Assume the existence of a non-negative integer $m$, and of
    positive constants $L$ and $R$, such that for all $z$ with $|z|>R$
    the inequality $$|f(z)| \leq L |z|^m$$ holds. Prove that $f$ is a
    polynomial of degree $\leq m$.

(b) Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire
    function. Suppose that there exists a real number M such that for
    all $z\in {\mathbb C}$ $$\mbox{\textrm Re} (f) \leq M.$$ Prove that $f$
    must be a constant.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:**
1. (a) Prove that if an entire function $f$ satisfies $|f(z)| \leq L |z|^m$ for all $|z| > R$ (where $m \geq 0$ is an integer), then $f$ is a polynomial of degree at most $m$.
2. (b) Prove that if an entire function $f$ satisfies $\text{Re}(f(z)) \leq M$ for all $z \in \mathbb{C}$ and some real constant $M$, then $f$ is constant.

---

### Part (a): Polynomial Bound via Cauchy's Estimates

<1>1. **Taylor expansion and Cauchy's Estimates.**
  <2>1. Since $f$ is entire, $f(z) = \sum_{k=0}^\infty c_k z^k$ for all $z \in \mathbb{C}$, where $c_k = \frac{f^{(k)}(0)}{k!}$.
    *Proof:* Fundamental theorem on power series of entire functions.
  <2>2. By Cauchy's Integral Formula for derivatives, for any circle $|z| = r > R$:
  $$c_k = \frac{1}{2\pi i} \oint_{|z|=r} \frac{f(z)}{z^{k+1}} \, dz.$$
    *Proof:* Cauchy's coefficient integral formula.
  <2>3. Applying the $ML$-inequality on $|z| = r > R$:
  $$|c_k| \leq \frac{1}{2\pi} \cdot \left( \sup_{|z|=r} \frac{|f(z)|}{|z|^{k+1}} \right) \cdot (2\pi r) \leq \frac{L r^m}{r^{k+1}} \cdot r = L r^{m-k}.$$
    *Proof:* On $|z| = r > R$, $|f(z)| \leq L r^m$.
  <2>4. Q.E.D.

<1>2. **Vanishing of coefficients $c_k$ for $k > m$.**
  <2>1. For any $k \geq m + 1$, the exponent $m - k \leq -1 < 0$.
    *Proof:* $k \geq m+1 \implies m - k \leq -1$.
  <2>2. Since the bound $|c_k| \leq L r^{m-k}$ holds for arbitrarily large $r > R$, taking the limit as $r \to \infty$:
  $$|c_k| \leq \lim_{r \to \infty} L r^{m-k} = 0.$$
    *Proof:* $r^{-p} \to 0$ as $r \to \infty$ for $p \geq 1$.
  <2>3. Therefore, $c_k = 0$ for all $k \geq m + 1$.
    *Proof:* Non-negative modulus bounded by 0 is 0.
  <2>4. Hence $f(z) = \sum_{k=0}^m c_k z^k$ is a polynomial of degree $\leq m$.
    *Proof:* Finite truncation of Taylor series.
  <2>5. Q.E.D.

---

### Part (b): Entire Function with Bounded Real Part

<1>3. **Construct an auxiliary entire function using the exponential map.**
  <2>1. Define $g(z) = e^{f(z)}$.
    *Proof:* Composition of the entire exponential function with the entire function $f$.
  <2>2. The modulus of $g(z)$ is:
  $$|g(z)| = |e^{f(z)}| = e^{\text{Re}(f(z))}.$$
    *Proof:* For any $w \in \mathbb{C}$, $|e^w| = e^{\text{Re}(w)}$.
  <2>3. By hypothesis, $\text{Re}(f(z)) \leq M$ for all $z \in \mathbb{C}$.
    *Proof:* Given assumption.
  <2>4. Since the exponential function $x \mapsto e^x$ is strictly increasing on $\mathbb{R}$:
  $$|g(z)| = e^{\text{Re}(f(z))} \leq e^M < \infty \quad \text{for all } z \in \mathbb{C}.$$
    *Proof:* Monotonicity of the real exponential.
  <2>5. Thus $g(z)$ is a bounded entire function on $\mathbb{C}$.
    *Proof:* Follows from <2>1 and <2>4.
  <2>6. Q.E.D.

<1>4. **Apply Liouville's Theorem to $g(z)$ and deduce $f(z)$ is constant.**
  <2>1. By Liouville's Theorem, every bounded entire function is constant, so there exists $C \in \mathbb{C}$ such that $g(z) = C$ for all $z \in \mathbb{C}$.
    *Proof:* Liouville's Theorem.
  <2>2. Since $g(z) = e^{f(z)} \neq 0$, the constant $C \neq 0$.
    *Proof:* The exponential function never vanishes.
  <2>3. Differentiating $e^{f(z)} = C$ with respect to $z$:
  $$f'(z) e^{f(z)} = 0 \implies f'(z) \cdot C = 0 \implies f'(z) = 0 \quad \text{for all } z \in \mathbb{C}.$$
    *Proof:* Chain rule and $C \neq 0$.
  <2>4. An entire function whose derivative vanishes identically on the connected domain $\mathbb{C}$ is constant.
    *Proof:* Fundamental theorem of calculus / connectedness of $\mathbb{C}$.
  <2>5. Therefore, $f(z)$ is constant.
    *Proof:* Conclusion of the argument.
  <2>6. Q.E.D.
:::
