---
schema: qual/card@1
id: E-GMYE2
kind: exercise
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
---

::: exercise
- Find a function that is differentiable but not continuously differentiable.

- Prove the **uniform limit theorem**: a uniform limit of continuous function is continuous.

- Show that the uniform limit of bounded functions is uniformly bounded.

- Construct sequences of functions $\ts{f_n}_{n\in \NN}$ and $\ts{g_n}_{n\in \NN}$ which converge uniformly on some set $E$, and yet their product sequence $\ts{h_n}_{n\in \NN}$ with $h_n \da f_n g_n$ does *not* converge uniformly.

  - Show that if $f_n, g_n$ are additionally bounded, then $h_n$ does converge uniformly.

- Find a sequence of functions such that $$\frac{d}{d x} \lim _{n \rightarrow \infty} f_{n}(x) \neq \lim _{n \rightarrow \infty} \frac{d}{d x} f_{n}(x)$$

- Find a uniform limit of differentiable functions that is not differentiable.

- Prove that the Cantor set is a Borel set.

- Show the Cantor ternary set is totally disconnected; that is show it contains no nonempty open interval.

- ![](../../assets/Workshops/Real%20Analysis/_attachments/Pasted%20image%2020210519152250.png)

- ![](../../assets/Workshops/Real%20Analysis/_attachments/Pasted%20image%2020210519151915.png)
:::

::: {.solution}
<1>1. A function differentiable but not continuously differentiable: $f(x) = x^2\sin(1/x)$ for $x \ne 0$, $f(0) = 0$.
<2>1. $f$ is differentiable everywhere, with $f'(0) = 0$.
::: {.proof}
$\frac{f(h) - f(0)}{h} = h\sin(1/h) \to 0$ as $h \to 0$ (bounded factor); away from $0$ differentiability is standard.
:::
<2>2. $f'$ is discontinuous at $0$.
::: {.proof}
for $x \ne 0$, $f'(x) = 2x\sin(1/x) - \cos(1/x)$, which has no limit as $x \to 0$ (the $\cos(1/x)$ term oscillates), while $f'(0) = 0$; hence $f$ is not $C^1$.
:::
<2>3. Q.E.D.
::: {.proof}
<2>1 and <2>2.
:::

<1>2. Uniform limit theorem: a uniform limit of continuous functions is continuous.
<2>1. Fix $x_0$ and $\eps > 0$; choose $n$ with $\|f - f_n\|_\infty < \eps/3$.
::: {.proof}
uniform convergence.
:::
<2>2. Choose $\delta > 0$ with $|f_n(x) - f_n(x_0)| < \eps/3$ for $|x - x_0| < \delta$.
::: {.proof}
continuity of $f_n$.
:::
<2>3. Then $|f(x) - f(x_0)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(x_0)| + |f_n(x_0) - f(x_0)| < \eps$.
::: {.proof}
triangle inequality, <2>1, <2>2. <2>4. Q.E.D. Proof: <2>3.
:::

<1>3. A uniform limit of bounded functions is uniformly bounded.
::: {.proof}
choose $N$ with $\|f - f_N\|_\infty \le 1$; then $\|f\|_\infty \le \|f_N\|_\infty + 1$.
:::

<1>4. Products of uniformly convergent sequences need not converge uniformly; they do if the sequences are bounded.
<2>1. Unbounded counterexample on $E = [1, \infty)$: $f_n(x) = x + \frac{1}{n}$, $g_n(x) = x$.
::: {.proof}
$f_n \to x$ uniformly ($\sup_{x\ge1}|x + 1/n - x| = 1/n \to 0$) and $g_n \to x$ uniformly (constant sequence); but $h_n = f_n g_n = x^2 + \frac{x}{n}$ has $\sup_{x\ge1}|h_n(x) - x^2| = \sup_{x\ge1}\frac{x}{n} = \infty \not\to 0$.
:::
<2>2. If $f_n \to f$ and $g_n \to g$ uniformly and all are bounded: $|f_n g_n - fg| \le |f_n|\,|g_n - g| + |g|\,|f_n - f| \le M\|g_n - g\|_\infty + M\|f_n - f\|_\infty \to 0$.
::: {.proof}
$|f_n| \le M$ and $|g| \le M$ uniformly (by <1>3-type boundedness: $f_n$ bounded since it converges uniformly to bounded $f$; $g$ bounded as a uniform limit of bounded functions).
:::
<2>3. Q.E.D.
::: {.proof}
<2>1 and <2>2.
:::

<1>5. A sequence with $\frac{d}{dx}\lim_n f_n \ne \lim_n \frac{d}{dx}f_n$: $f_n(x) = \frac{\sin(nx)}{n}$.
::: {.proof}
$f_n \to 0$ uniformly, so $\frac{d}{dx}\lim_n f_n(x) = 0$; but $f_n'(x) = \cos(nx)$ and $\lim_n f_n'(0) = \lim_n 1 = 1 \ne 0$ — the derivative limit does not exist pointwise for $x \ne 0$ and disagrees with the derivative of the limit at $x = 0$.
:::

<1>6. A uniform limit of differentiable functions that is not differentiable: $f_n(x) = \sqrt{x^2 + \frac{1}{n}}$ on $\RR$.
<2>1. $f_n \to |x|$ uniformly.
::: {.proof}
$0 \le \sqrt{x^2 + 1/n} - |x| = \frac{1/n}{\sqrt{x^2 + 1/n} + |x|} \le \frac{1/n}{\sqrt{1/n}} = \frac{1}{\sqrt n} \to 0$.
:::
<2>2. Each $f_n$ is smooth, but $|x|$ is not differentiable at $0$.
::: {.proof}
$x \mapsto \sqrt{x^2 + c}$ is smooth for $c > 0$; $|x|$ has different left and right derivatives at $0$.
:::
<2>3. Q.E.D.
::: {.proof}
<2>1 and <2>2.
:::

<1>7. The Cantor set is a Borel set.
::: {.proof}
the Cantor set is closed: $C = \bigcap_n C_n$ with each $C_n$ a finite union of closed intervals; closed sets are Borel.
:::

<1>8. The Cantor ternary set is totally disconnected: it contains no nonempty open interval.
::: {.proof}
$m^*(C) \le m(C_n) = (2/3)^n$ for all $n$, so $m(C) = 0$; an open interval has positive measure, so no interval is contained in $C$.
:::
(Equivalently, every point's ternary expansion has only digits $0,2$, and any two distinct points are separated by a removed middle third.)
:::
