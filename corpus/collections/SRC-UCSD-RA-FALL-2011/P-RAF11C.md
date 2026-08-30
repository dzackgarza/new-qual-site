---
schema: qual/card@1
id: P-RAF11C
kind: problem
title: "Uniform integrability and convergence in L^1"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
(a) Let $(X, \mathcal{M}, \mu)$ be a finite measure space.
Suppose that $f_n \in L^1(d\mu)$ is a sequence of functions with the property that for every $\epsilon > 0$ there exists a $\delta > 0$ such that for all $E \in \mathcal{M}$:
$$
|E| < \delta \implies \sup_n \int_E |f_n|\,d\mu < \epsilon.
$$
Suppose in addition that there exists $f$ with $f_n \to f$ $\mu$-a.e. Show that $f_n \to f$ in $L^1(d\mu)$.

(b) Give a simple example to show that if one drops the finite measure assumption but keeps all the other hypotheses above, the conclusion can fail.
:::

::: {.solution}
<1>1. Part (a): $L^1$ convergence under uniform integrability on finite measure spaces:
<2>1. First we establish $f \in L^1(d\mu)$ and uniform integrability of $|f_n - f|$:
- Since $\mu(X) < \infty$, partition $X$ into a finite number of sets $E_1, \dots, E_k$ each of measure $< \delta_1$ (where $\delta_1$ corresponds to $\epsilon = 1$).
  Then $\sup_n \int_X |f_n| \, d\mu \le \sum_{j=1}^k \sup_n \int_{E_j} |f_n| \, d\mu \le k < \infty$.
- By Fatou's Lemma, $\int_X |f| \, d\mu \le \liminf_{n\to\infty} \int_X |f_n| \, d\mu \le k < \infty$, so $f \in L^1(d\mu)$.
- For any $E \in \mathcal{M}$ with $\mu(E) < \delta$:
\[
\int_E |f| \, d\mu \le \liminf_{n \to \infty} \int_E |f_n| \, d\mu \le \epsilon.
\]
Thus $\sup_n \int_E |f_n - f| \, d\mu \le \sup_n \int_E |f_n| \, d\mu + \int_E |f| \, d\mu < 2\epsilon$.
Proof: Fatou's Lemma and triangle inequality.
<2>2. Let $\varepsilon > 0$ be given. Choose $\delta > 0$ such that $\mu(E) < \delta \implies \sup_n \int_E |f_n - f| \, d\mu < \varepsilon$.
Because $\mu(X) < \infty$ and $f_n \to f$ a.e., by Egorov's Theorem there exists a measurable set $E \in \mathcal{M}$ such that $\mu(E) < \delta$ and $f_n \to f$ uniformly on $X \setminus E$.
Proof: Egorov's Theorem on finite measure spaces.
<2>3. Decompose the $L^1$ norm of $f_n - f$:
\[
\int_X |f_n - f| \, d\mu = \int_{X \setminus E} |f_n - f| \, d\mu + \int_E |f_n - f| \, d\mu.
\]
Proof: additivity of the Lebesgue integral.
<2>4. Estimate each term:
- On $X \setminus E$, $f_n \to f$ uniformly, so $\lim_{n \to \infty} \int_{X \setminus E} |f_n - f| \, d\mu \le \lim_{n \to \infty} \|f_n - f\|_{L^\infty(X \setminus E)} \mu(X) = 0$.
- On $E$, since $\mu(E) < \delta$, $\int_E |f_n - f| \, d\mu < \varepsilon$ for all $n$.
Proof: uniform convergence and choice of $\delta$.
<2>5. Taking the limit superior:
\[
\limsup_{n \to \infty} \int_X |f_n - f| \, d\mu \le 0 + \varepsilon = \varepsilon.
\]
Since $\varepsilon > 0$ was arbitrary, $\lim_{n \to \infty} \|f_n - f\|_{L^1(d\mu)} = 0$.
Proof: definition of limit.

<1>2. Part (b): Counterexample when $\mu(X) = \infty$:
<2>1. Let $X = \mathbb{R}$ equipped with the standard Lebesgue measure $m$, so $m(\mathbb{R}) = \infty$.
Define $f_n(x) = \mathbf{1}_{[n, n+1]}(x)$ for $n \ge 1$.
Proof: well-defined sequence in $L^1(\mathbb{R})$.
<2>2. For any $\varepsilon > 0$, choose $\delta = \varepsilon$.
For every measurable set $E \subseteq \mathbb{R}$ with $m(E) < \delta$:
\[
\sup_{n} \int_E |f_n| \, dm = \sup_n m(E \cap [n, n+1]) \le m(E) < \varepsilon.
\]
Thus $(f_n)$ satisfies the uniform integrability hypothesis.
Proof: monotonicity of Lebesgue measure.
<2>3. For every $x \in \mathbb{R}$, $f_n(x) = 0$ for all $n > x$, so $f_n \to 0$ pointwise everywhere as $n \to \infty$.
However:
\[
\|f_n - 0\|_{L^1(\mathbb{R})} = \int_\mathbb{R} \mathbf{1}_{[n, n+1]}(x) \, dx = 1 \quad \text{for all } n \ge 1.
\]
Thus $f_n \not\to 0$ in $L^1(\mathbb{R})$.
Proof: integration of indicator functions.

<1>3. Conclusion:
$f_n \to f$ in $L^1$ on finite measure spaces, and $f_n = \mathbf{1}_{[n, n+1]}$ provides a counterexample on infinite measure spaces. Q.E.D.
Proof: <1>1 and <1>2.
:::
