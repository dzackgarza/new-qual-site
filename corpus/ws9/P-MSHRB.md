---
schema: qual/card@1
id: P-MSHRB
kind: problem
title: "a. Prove that the operator $T : L^2([0,1]) \\to L^2([0,1])$ defined by…"
classification:
  areas:
  - real-analysis
  topics:
  - functional-analysis
  - l2
  - compactness
relations: []
review: draft
---

::: {.problem title="?"}
a. Prove that the operator $T : L^2([0,1]) \to L^2([0,1])$ defined by setting $T[f](x) = xf(x)$ is continuous and symmetric (self-adjoint).
b. Prove that $T$ is not compact.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. (a) $T$ is continuous.
    Proof: for $f \in L^2([0,1])$,
    \[\|Tf\|_{L^2}^2 = \int_0^1 x^2|f(x)|^2\,dx \le \int_0^1 |f(x)|^2\,dx = \|f\|_{L^2}^2,\]
    so $\|T\| \le 1$; $T$ is linear, hence bounded and continuous.
<1>2. (a) $T$ is symmetric.
    Proof: for $f, g \in L^2([0,1])$,
    \[\langle Tf, g\rangle = \int_0^1 xf(x)\overline{g(x)}\,dx = \int_0^1 f(x)\overline{xg(x)}\,dx = \langle f, Tg\rangle,\]
    as $x$ is real. Thus $T = T^*$.
<1>3. (b) $T$ is not compact.
    Proof: for $n \ge 1$ put $I_n = [1 - 1/n,\; 1 - 1/(n+1))$ and $f_n = \sqrt{n(n+1)}\,\mathbf 1_{I_n}$. The intervals $I_n$ partition $[0,1)$ and $\|f_n\|_{L^2}^2 = n(n+1)\cdot\left(\frac{1}{n} - \frac{1}{n+1}\right) = 1$, so $\{f_n\}$ is an orthonormal sequence. On $I_n$ we have $x \ge 1 - 1/n$, so
    \[\|Tf_n\|_{L^2}^2 = \int_{I_n}x^2|f_n|^2\,dx \ge \left(1 - \frac1n\right)^2 \to 1.\]
    If $T$ were compact, the bounded sequence $\{Tf_n\}$ would have a convergent subsequence. But $Tf_n$ and $Tf_m$ have disjoint supports for $n \ne m$, so $\|Tf_n - Tf_m\|_{L^2}^2 = \|Tf_n\|^2 + \|Tf_m\|^2 \ge (1-\frac1n)^2 + (1-\frac1m)^2 \ge \frac12$ for all large $n \ne m$; no subsequence can be Cauchy. Hence $T$ is not compact.
<1>4. Q.E.D.
:::
