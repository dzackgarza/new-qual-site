---
schema: qual/card@1
id: E-GMYE2
kind: problem
title: Uniform limits, differentiability counterexamples, and the Cantor set
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Differentiation
  - Cantor Set
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: Parts (i)-(m) were embedded as two screenshots (assets/Workshops/Real Analysis/_attachments/Pasted image 20210519152250.png and Pasted image 20210519151915.png); they are transcribed from the images and checked against the workshop sheet assets/Workshops/Real Analysis/RealWeek1.pdf (items I.7 and the preceding list), whose item I.7 has exactly the two conditions of part (m).
- event: solution-written
  by: claude-opus-5.5
  date: 2026-10-29
  note: Solution steps for parts (i)-(m).
---

::: {.exercise}
(a) Find a function that is differentiable but not continuously differentiable.

(b) Prove the **uniform limit theorem**: a uniform limit of continuous functions is continuous.

(c) Show that the uniform limit of bounded functions is uniformly bounded.

(d) Construct sequences of functions $\theset{f_n}_{n\in \NN}$ and $\theset{g_n}_{n\in \NN}$ which converge uniformly on some set $E$, and yet their product sequence $\theset{h_n}_{n\in \NN}$ with $h_n \definedas f_n g_n$ does *not* converge uniformly.
Show that if $f_n, g_n$ are additionally bounded, then $h_n$ does converge uniformly.

(e) Find a sequence of functions such that $$\frac{d}{d x} \lim _{n \rightarrow \infty} f_{n}(x) \neq \lim _{n \rightarrow \infty} \frac{d}{d x} f_{n}(x).$$

(f) Find a uniform limit of differentiable functions that is not differentiable.

(g) Prove that the Cantor set is a Borel set.

(h) Show the Cantor ternary set is totally disconnected; that is, show it contains no nonempty open interval.

(i) Show the set of irrational numbers is a $G_\delta$ set but is not an $F_\sigma$ set.
Hint: show $\QQ$ is not a $G_\delta$, for otherwise one could obtain a decreasing sequence $G_n$ of dense open sets that have empty intersection; then use the decomposition of each $G_n$ into a disjoint countable union of open intervals.

(j) Using the fact that the set of rational numbers in any closed interval $a \le x \le b$ where $a < b$ is not a $G_\delta$ set, give an example of a Borel subset of $\RR$ which is neither an $F_\sigma$ nor a $G_\delta$ set.

(k) Let $f$ be any function from $\RR$ to $\RR$. Prove that the set of points of discontinuity of $f$ is of type $F_\sigma$.

(l) Can a function from $\RR$ to $\RR$ be continuous on the rationals and discontinuous on the irrationals? What if the roles of the rationals and irrationals are interchanged?

(m) Let $(x_n)_{n\in\NN}$ be a sequence of real numbers. Prove that the following are equivalent:

1. $\lim_{n\to\infty} x_n = a$.

2. Every subsequence of $(x_n)_{n\in\NN}$ contains a subsequence that converges to $a$.
:::

::: {.solution}

::: pf

::: pf-step

(a) $f(x) = x^2\sin(1/x)$ for $x \ne 0$, $f(0) = 0$, is differentiable on $\RR$ but not continuously differentiable.

::: pf-proof

::: pf-step

$f$ is differentiable everywhere, with $f'(0) = 0$ and $f'(x) = 2x\sin(1/x) - \cos(1/x)$ for $x \neq 0$.

::: pf-proof

$\frac{f(h) - f(0)}{h} = h\sin(1/h)$ and $|h\sin(1/h)| \leq |h| \to 0$. For $x \neq 0$, $f$ is a product and composition of differentiable functions near $x$, and the product and chain rules give the formula.

:::

:::

::: pf-step

$f'$ is discontinuous at $0$.

::: pf-proof

At $x_k = 1/(2k\pi)$, $f'(x_k) = -1$ for every $k$, while $x_k \to 0$ and $f'(0) = 0$.

:::

:::

:::

:::

::: pf-step

(b) If $f_n \to f$ uniformly on $E$ and each $f_n$ is continuous, then $f$ is continuous.

::: pf-proof

::: {.pf-step #s2-1}

Fix $x_0 \in E$ and $\eps > 0$. There are $n$ with $\|f - f_n\|_\infty < \eps/3$ and $\delta > 0$ with $|f_n(x) - f_n(x_0)| < \eps/3$ for $x \in E$, $|x - x_0| < \delta$.

::: pf-proof

The first is uniform convergence; the second is continuity of $f_n$ at $x_0$.

:::

:::

::: pf-qed

For $x \in E$ with $|x - x_0| < \delta$, step [](#s2-1){.pf-ref} and the triangle inequality give $|f(x) - f(x_0)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(x_0)| + |f_n(x_0) - f(x_0)| < \eps$.

:::

:::

:::

::: {.pf-step #s3}

(c) If $f_n \to f$ uniformly and each $f_n$ is bounded, then $f$ is bounded, and $\sup_{n}\|f_n\|_\infty < \infty$.

::: pf-proof

Choose $N$ with $\|f - f_n\|_\infty \le 1$ for $n \geq N$. Then $\|f\|_\infty \le \|f_N\|_\infty + 1$, and $\|f_n\|_\infty \leq \|f\|_\infty + 1$ for $n \geq N$, so $\sup_n \|f_n\|_\infty \leq \max(\|f_1\|_\infty, \ldots, \|f_{N-1}\|_\infty, \|f\|_\infty + 1)$.

:::

:::

::: pf-step

(d) Products of uniformly convergent sequences need not converge uniformly; they do if every $f_n$ and $g_n$ is bounded.

::: pf-proof

::: pf-step

On $E = [1, \infty)$, $f_n(x) = x + \frac{1}{n}$ and $g_n(x) = x$ converge uniformly, but $h_n = f_n g_n$ does not.

::: pf-proof

$\sup_{x\ge1}|f_n(x) - x| = 1/n \to 0$, and $g_n$ is constant in $n$. But $h_n(x) = x^2 + \frac{x}{n} \to x^2$ pointwise, and $\sup_{x\ge1}|h_n(x) - x^2| = \sup_{x\ge1}\frac{x}{n} = \infty$ for every $n$.

:::

:::

::: pf-step

If $f_n \to f$ and $g_n \to g$ uniformly and every $f_n$ and $g_n$ is bounded, then $f_n g_n \to fg$ uniformly.

::: pf-proof

By step [](#s3){.pf-ref}, $g$ is bounded and there is $M$ with $\|f_n\|_\infty \le M$ for all $n$ and $\|g\|_\infty \le M$. Then $|f_n g_n - fg| \le |f_n|\,|g_n - g| + |g|\,|f_n - f| \le M\|g_n - g\|_\infty + M\|f_n - f\|_\infty \to 0$ uniformly on $E$.

:::

:::

:::

:::

::: pf-step

(e) $f_n(x) = \frac{\sin(nx)}{n}$ satisfies $\frac{d}{dx}\lim_n f_n \ne \lim_n \frac{d}{dx}f_n$ at $x = 0$.

::: pf-proof

$|f_n| \leq 1/n$, so $f_n \to 0$ uniformly and $\frac{d}{dx}\lim_n f_n(x) = 0$. But $f_n'(x) = \cos(nx)$, so $\lim_n f_n'(0) = 1 \ne 0$.

:::

:::

::: pf-step

(f) $f_n(x) = \sqrt{x^2 + \frac{1}{n}}$ are differentiable on $\RR$ and converge uniformly to $|x|$, which is not differentiable at $0$.

::: pf-proof

::: pf-step

$f_n \to |x|$ uniformly.

::: pf-proof

$0 \le \sqrt{x^2 + 1/n} - |x| = \frac{1/n}{\sqrt{x^2 + 1/n} + |x|} \le \frac{1/n}{\sqrt{1/n}} = \frac{1}{\sqrt n} \to 0$.

:::

:::

::: pf-step

Each $f_n$ is smooth, and $|x|$ is not differentiable at $0$.

::: pf-proof

$x \mapsto \sqrt{x^2 + c}$ is smooth for $c > 0$, since $x^2 + c > 0$. The function $|x|$ has left derivative $-1$ and right derivative $1$ at $0$.

:::

:::

:::

:::

::: pf-step

(g) The Cantor set $C$ is a Borel set.

::: pf-proof

$C = \bigcap_n C_n$, where $C_n$ is the union of the $2^n$ closed intervals of length $3^{-n}$ remaining after $n$ stages. Each $C_n$ is closed, so $C$ is closed, and closed sets are Borel.

:::

:::

::: pf-step

(h) $C$ contains no nonempty open interval.

::: pf-proof

$m(C) \le m(C_n) = (2/3)^n$ for all $n$, so $m(C) = 0$. A nonempty open interval has positive measure, so it is not contained in $C$.

:::

:::

::: pf-step

(i) The set $\RR \setminus \QQ$ of irrational numbers is a $G_\delta$ set and is not an $F_\sigma$ set.

::: pf-proof

::: pf-step

$\RR \setminus \QQ$ is a $G_\delta$ set.

::: pf-proof

$\RR \setminus \QQ = \bigcap_{q \in \QQ} (\RR \setminus \theset{q})$ is a countable intersection of open sets.

:::

:::

::: {.pf-step #q-not-gdelta}

$\QQ$ is not a $G_\delta$ set.

::: pf-proof

Suppose $\QQ = \bigcap_{n} G_n$ with each $G_n$ open. Each $G_n$ contains $\QQ$, so it is dense. Each $\RR \setminus \theset{q}$ with $q \in \QQ$ is also open and dense. The countable family $\theset{G_n}_n \cup \theset{\RR \setminus \theset{q}}_{q \in \QQ}$ of dense open sets has intersection $\QQ \cap (\RR \setminus \QQ) = \emptyset$. This contradicts the Baire category theorem for the complete metric space $\RR$.

:::

:::

::: pf-qed

If $\RR \setminus \QQ$ were $F_\sigma$, its complement $\QQ$ would be $G_\delta$, which step [](#q-not-gdelta){.pf-ref} excludes.

:::

:::

:::

::: pf-step

(j) The set $A \coloneqq (\QQ \cap [0,1]) \cup ([2,3] \setminus \QQ)$ is a Borel set that is neither $F_\sigma$ nor $G_\delta$.

::: pf-proof

::: {.pf-step #irr-not-fsigma}

$[2,3] \setminus \QQ$ is not an $F_\sigma$ set.

::: pf-proof

If $[2,3] \setminus \QQ = F$ with $F$ an $F_\sigma$ set, then $\QQ \cap [2,3] = [2,3] \cap (\RR \setminus F)$. The closed set $[2,3]$ is a $G_\delta$ set and $\RR \setminus F$ is a $G_\delta$ set, so $\QQ \cap [2,3]$ is a $G_\delta$ set, contrary to the given fact.

:::

:::

::: pf-step

$A$ is Borel, $A$ is not $G_\delta$, and $A$ is not $F_\sigma$.

::: pf-proof

$\QQ \cap [0,1]$ is countable, hence $F_\sigma$, and $[2,3] \setminus \QQ$ is the intersection of a closed set with the $G_\delta$ set $\RR \setminus \QQ$; so $A$ is Borel. A closed set is both $F_\sigma$ and $G_\delta$, and both classes are closed under finite intersections. If $A$ were $G_\delta$, then $A \cap [0,1] = \QQ \cap [0,1]$ would be $G_\delta$, contrary to the given fact. If $A$ were $F_\sigma$, then $A \cap [2,3] = [2,3] \setminus \QQ$ would be $F_\sigma$, contrary to step [](#irr-not-fsigma){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #disc-fsigma}

(k) For every $f\colon \RR \to \RR$, the set $D_f$ of points of discontinuity of $f$ is an $F_\sigma$ set.

::: pf-proof

::: {.pf-step #osc-zero}

With the oscillation $\omega_f(x) \coloneqq \inf_{\delta > 0} \sup\theset{\abs{f(y) - f(z)} : y, z \in (x - \delta, x + \delta)}$, $f$ is continuous at $x$ if and only if $\omega_f(x) = 0$.

::: pf-proof

If $f$ is continuous at $x$ and $\varepsilon > 0$, choose $\delta$ with $\abs{f(y) - f(x)} < \varepsilon/2$ for $\abs{y - x} < \delta$; then all $y, z \in (x - \delta, x + \delta)$ satisfy $\abs{f(y) - f(z)} < \varepsilon$, so $\omega_f(x) \le \varepsilon$. Conversely, if $\omega_f(x) < \varepsilon$, some $\delta$ gives $\abs{f(y) - f(x)} < \varepsilon$ for $\abs{y - x} < \delta$.

:::

:::

::: {.pf-step #osc-closed}

For each $\varepsilon > 0$ the set $\theset{x : \omega_f(x) \ge \varepsilon}$ is closed.

::: pf-proof

Let $\omega_f(x) < \varepsilon$, and choose $\delta > 0$ with $\sup\theset{\abs{f(y) - f(z)} : y, z \in (x - \delta, x + \delta)} < \varepsilon$. For $\abs{x' - x} < \delta/2$ the interval $(x' - \delta/2, x' + \delta/2)$ lies in $(x - \delta, x + \delta)$, so $\omega_f(x') < \varepsilon$. The complement is therefore open.

:::

:::

::: pf-qed

By step [](#osc-zero){.pf-ref}, $D_f = \bigcup_{n \ge 1} \theset{x : \omega_f(x) \ge 1/n}$, a countable union of sets that are closed by step [](#osc-closed){.pf-ref}.

:::

:::

:::

::: pf-step

(l) No function $\RR \to \RR$ is continuous exactly on $\QQ$. The function $t$ with $t(p/q) \coloneqq 1/q$ for $p/q$ in lowest terms with $q \ge 1$, and $t(x) \coloneqq 0$ for $x \notin \QQ$, is continuous exactly on $\RR \setminus \QQ$.

::: pf-proof

::: pf-step

No function is continuous on $\QQ$ and discontinuous on $\RR \setminus \QQ$.

::: pf-proof

Its set of discontinuities would be $\RR \setminus \QQ$, which is $F_\sigma$ by step [](#disc-fsigma){.pf-ref}; part (i) shows that it is not.

:::

:::

::: pf-step

$t$ is discontinuous at each rational point.

::: pf-proof

At $x = p/q$, $t(x) = 1/q > 0$, while irrational points $y \to x$ have $t(y) = 0$.

:::

:::

::: pf-step

$t$ is continuous at each irrational point.

::: pf-proof

Let $x \notin \QQ$ and $\varepsilon > 0$. The interval $(x - 1, x + 1)$ contains finitely many rationals $p/q$ with $q \le 1/\varepsilon$, and none of them equals $x$. Choose $\delta \in (0,1)$ smaller than the distance from $x$ to each of them. Every $y$ with $\abs{y - x} < \delta$ is irrational or equals $p/q$ in lowest terms with $q > 1/\varepsilon$, so $\abs{t(y) - t(x)} = t(y) < \varepsilon$.

:::

:::

:::

:::

::: pf-step

(m) $\lim_{n \to \infty} x_n = a$ if and only if every subsequence of $(x_n)_{n \in \NN}$ contains a subsequence that converges to $a$.

::: pf-proof

::: pf-step

If $x_n \to a$, every subsequence has a subsequence that converges to $a$.

::: pf-proof

Every subsequence of a sequence that converges to $a$ converges to $a$, and it is a subsequence of itself.

:::

:::

::: pf-step

If every subsequence has a subsequence that converges to $a$, then $x_n \to a$.

::: pf-proof

Suppose $x_n \not\to a$. Then there are $\varepsilon > 0$ and indices $n_1 < n_2 < \cdots$ with $\abs{x_{n_k} - a} \ge \varepsilon$ for all $k$. Every subsequence of $(x_{n_k})_k$ stays at distance at least $\varepsilon$ from $a$, so none converges to $a$, contrary to the hypothesis.

:::

:::

:::

:::

:::

:::
