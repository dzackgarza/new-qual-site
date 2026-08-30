---
schema: qual/card@1
id: P-4KTFN
kind: problem
title: "Fatou's lemma, the dominated convergence theorem, and a counterexample"
classification:
  areas:
  - real-analysis
  topics:
  - Fatou's Lemma
  - Dominated Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

6. For this problem, consider just Lebesgue measurable functions $f : [ 0 , 1 ] \to \mathbb { R }$ . together with the Lebesgue measure.

(a) State Fatou’s lemma (no proof required).

(b) State and prove the Dominated Convergence Theorem.

(c) Give an example where $f _ { n } ( x )  0 { \mathrm { ~ a . e . } }$ , but $\textstyle \int _ { - \infty } ^ { + \infty } f _ { n } ( x ) d x \to 1$

::: {.solution}
<1>1. Part (a): Statement of Fatou’s Lemma:
<2>1. **Fatou's Lemma:** Let $(X, \mathcal{M}, \mu)$ be a measure space, and let $\{f_n\}_{n=1}^\infty$ be a sequence of non-negative measurable functions $f_n: X \to [0, \infty]$. Then:
\[
\int_X \liminf_{n \to \infty} f_n \, d\mu \le \liminf_{n \to \infty} \int_X f_n \, d\mu.
\]
Proof: statement of Fatou's Lemma.

<1>2. Part (b): Statement and Proof of the Dominated Convergence Theorem:
<2>1. **Statement:** Let $\{f_n\}$ be a sequence of measurable functions on $(X, \mu)$ converging pointwise almost everywhere to $f$.
If there exists an integrable function $g \in L^1(X, \mu)$ such that $|f_n(x)| \le g(x)$ for almost every $x$ and all $n \ge 1$, then $f \in L^1(X, \mu)$ and:
\[
\lim_{n \to \infty} \int_X f_n \, d\mu = \int_X f \, d\mu.
\]
Proof: statement of DCT.
<2>2. **Proof:**
Since $|f_n(x)| \le g(x)$ a.e. and $f_n(x) \to f(x)$ a.e., taking $n \to \infty$ gives $|f(x)| \le g(x)$ a.e., so $f \in L^1(X, \mu)$.
Proof: monotonicity of limits and integrability of dominator.
<2>3. Consider the non-negative sequence $u_n = g + f_n \ge 0$.
Applying Fatou's Lemma to $\{u_n\}$:
\[
\int_X (g + f) \, d\mu = \int_X \liminf_{n \to \infty} (g + f_n) \, d\mu \le \liminf_{n \to \infty} \int_X (g + f_n) \, d\mu = \int_X g \, d\mu + \liminf_{n \to \infty} \int_X f_n \, d\mu.
\]
Subtracting the finite value $\int_X g \, d\mu < \infty$:
\[
\int_X f \, d\mu \le \liminf_{n \to \infty} \int_X f_n \, d\mu.
\]
Proof: linearity of integrals and Fatou's Lemma.
<2>4. Symmetrically, consider the non-negative sequence $v_n = g - f_n \ge 0$.
Applying Fatou's Lemma to $\{v_n\}$:
\[
\int_X (g - f) \, d\mu = \int_X \liminf_{n \to \infty} (g - f_n) \, d\mu \le \liminf_{n \to \infty} \int_X (g - f_n) \, d\mu = \int_X g \, d\mu - \limsup_{n \to \infty} \int_X f_n \, d\mu.
\]
Subtracting $\int_X g \, d\mu$ and multiplying by $-1$:
\[
\limsup_{n \to \infty} \int_X f_n \, d\mu \le \int_X f \, d\mu.
\]
Proof: $\liminf(-a_n) = -\limsup(a_n)$.
<2>5. Combining <2>3 and <2>4:
\[
\limsup_{n \to \infty} \int_X f_n \, d\mu \le \int_X f \, d\mu \le \liminf_{n \to \infty} \int_X f_n \, d\mu.
\]
Since $\liminf \le \limsup$, all inequalities are equalities, establishing $\lim_{n \to \infty} \int_X f_n \, d\mu = \int_X f \, d\mu$.
Proof: squeeze principle.

<1>3. Part (c): Counterexample with vanishing pointwise limit and non-zero integral:
<2>1. Define $f_n: [0, 1] \to \mathbb{R}$ by:
\[
f_n(x) = n \, \mathbf{1}_{(0, 1/n)}(x) = \begin{cases} n & \text{if } 0 < x < 1/n, \\ 0 & \text{otherwise.} \end{cases}
\]
(Alternatively, $f_n(x) = \mathbf{1}_{[n, n+1]}(x)$ on $\mathbb{R}$).
Proof: explicit construction.
<2>2. **Pointwise limit:**
- If $x = 0$, $f_n(0) = 0$ for all $n$.
- If $x \in (0, 1]$, choose $N > 1/x$. For all $n \ge N$, $1/n < x$, so $f_n(x) = 0$.
Thus $f_n(x) \to 0$ for all $x \in [0, 1]$ (pointwise everywhere).
Proof: Archimedean property of $\mathbb{R}$.
<2>3. **Integral limit:**
For every $n \ge 1$:
\[
\int_0^1 f_n(x) \, dx = \int_0^{1/n} n \, dx = n \cdot \frac{1}{n} = 1.
\]
Thus $\lim_{n \to \infty} \int_0^1 f_n(x) \, dx = 1 \neq 0 = \int_0^1 \lim_{n \to \infty} f_n(x) \, dx$.
Proof: Riemann/Lebesgue integral of step functions.

<1>4. Conclusion:
Fatou's Lemma is stated, DCT is proven, and $f_n(x) = n \mathbf{1}_{(0, 1/n)}(x)$ provides the required example. Q.E.D.
Proof: <1>1 through <1>3.
:::
