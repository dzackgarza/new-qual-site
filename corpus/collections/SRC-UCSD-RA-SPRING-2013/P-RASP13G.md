---
schema: qual/card@1
id: P-RASP13G
kind: problem
title: "sin(kx) converges weakly but not strongly to zero in L^p"
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Lp Spaces
  - Riemann-Lebesgue Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $X = [-\pi, \pi]$ with Lebesgue measure.
Let $p$ be a real number with $1 \leq p < \infty$.
Define for each integer $k \geq 1$ that $f_k(x) = \sin(kx)$ ($x \in X$).

(a) Prove that the sequence $\{f_k\}$ converges weakly to $0$ in $L^p(X)$.

(b) Prove that the sequence $\{f_k\}$ does not converge to $0$ strongly in $L^p(X)$.
:::

::: {.solution}
**Part (a).**

<1>1. It suffices to show $\int_X f_k g \to 0$ for every $g$ in a dense subset of $L^q(X)$, where $\frac1p + \frac1q = 1$.
::: {.proof}
the $f_k$ are uniformly bounded in $L^p$ (since $|f_k| \le 1$ on the finite-measure set $X$), so weak convergence follows from convergence against a dense set of test functions.
:::

<1>2. For every $g \in C^1(X)$ (or any $g \in L^q$), $\int_{-\pi}^{\pi} \sin(kx)\, g(x)\, dx \to 0$.
::: {.proof}
this is the Riemann–Lebesgue lemma.
:::

<1>3. Hence $f_k \rightharpoonup 0$ in $L^p(X)$.
::: {.proof}
<1>1 and <1>2.
:::

**Part (b).**

<1>1. $\|f_k\|_{L^p}^p = \int_{-\pi}^{\pi} |\sin(kx)|^p\, dx$ is constant in $k$ and nonzero.
::: {.proof}
by periodicity, $\int_{-\pi}^{\pi} |\sin(kx)|^p\, dx = \int_{-\pi}^{\pi} |\sin(x)|^p\, dx > 0$ (substitute $u = kx$ and use $2\pi$-periodicity).
:::

<1>2. Hence $\|f_k\|_{L^p} \not\to 0$.
::: {.proof}
<1>1 shows the norm is a fixed positive constant.
:::

<1>3. Therefore $f_k$ does not converge strongly to $0$ in $L^p(X)$.
::: {.proof}
strong convergence to $0$ would force $\|f_k\|_{L^p} \to 0$, contradicting <1>2.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3 (part (a)) and <1>3 (part (b)).
:::
:::
