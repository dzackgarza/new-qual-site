---
schema: qual/card@1
id: P-GFCIL
kind: problem
title: $(C[0,1],\|\cdot\|_p)$ is not a Banach space, $L^p[0,1]$ is Banach, convolution
  has no smooth identity, Hölder's inequality, and Young's inequality $L^p*L^q\subset
  L^r$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Norms
  - Completeness
  - Convolution
relations: []
review: draft
---

::: {.problem title="?"}
Let $I = [0,1]$ and denote $\|\cdot\|_p$ the $p$-norm $\|f\|_p = \left(\int_I |f|^p\right)^{1/p}$ for $1 \le p < \infty$ (we admit this is a norm) and $\|f\|_\infty = \operatorname{ess\,sup}|f|$.

- Show that the space of continuous functions on $I$ endowed with the norm $\|\cdot\|_p$ for $1 \le p < \infty$ is not a Banach space.

- Prove that the space of (Lebesgue) measurable functions on $I$ such that their $p$-norm is finite is a Banach space for $1 \le p \le \infty$.

- Prove that there is no smooth function $h$ such that $f * h = f$ for every $f \in L^1(I)$.

- Prove the Hölder inequality: for $p, q \ge 1$ such that $\frac{1}{p}+\frac{1}{q}=1$ $$\int_I fg \le \|f\|_p\|g\|_q$$ One can use the inequality $ab \le \frac{a^p}{p}+\frac{a^q}{q}$ for any $a,b \ge 0$.

- Deduce the Young inequality: $L^p * L^q \subset L^r$ for $\frac{1}{p}+\frac{1}{q} = 1+\frac{1}{r}$
:::


::: {.solution}
> **AI-Generated Solution**

*Setup note.* For part 3, "identity for convolution" is interpreted on the circle $\RR/\ZZ$ (i.e. $f,h$ extended periodically); the other parts concern $I = [0,1]$ with Lebesgue measure.

<1>1. $(C(I), \|\cdot\|_p)$ is not a Banach space for $1 \le p < \infty$.
    Proof: it is not complete. The continuous tent functions $f_n(x) = \min(nx,\, 1,\, n(1-x))$ converge in $\|\cdot\|_p$ to the indicator $\chi_{[1/3,2/3]}$ (indeed $|f_n - \chi_{[1/3,2/3]}| \le 2$ with support shrinking to $\{1/3, 2/3\}$), so $(f_n)$ is $\|\cdot\|_p$-Cauchy. But its $L^p$ limit $\chi_{[1/3,2/3]}$ is discontinuous, so the limit does not lie in $C(I)$; hence $(f_n)$ has no limit in $C(I)$ and $C(I)$ is not complete.
<1>2. $(L^p(I), \|\cdot\|_p)$ is a Banach space for $1 \le p \le \infty$.
    Proof: for $1 \le p < \infty$: let $(f_n)$ be $\|\cdot\|_p$-Cauchy. By Chebyshev's inequality $m\{|f_n - f_m| > \delta\} \le \|f_n - f_m\|_p^p/\delta^p$, the sequence is Cauchy in measure, so a subsequence converges pointwise a.e. to a measurable $f$. Fatou's lemma gives $\int|f|^p \le \liminf_n\int|f_n|^p < \infty$, so $f \in L^p$; and for $\eps > 0$, choosing $N$ with $\|f_n - f_m\|_p < \eps$ for $n, m \ge N$ and using Fatou again,
    \[
    \|f_n - f\|_p \le \liminf_{m\to\infty}\|f_n - f_m\|_p \le \eps ,
    \]
    so $f_n \to f$ in $L^p$. For $p = \infty$: a $\|\cdot\|_\infty$-Cauchy sequence is uniformly Cauchy off a null set $E$; on $I\setminus E$ it converges uniformly to a bounded measurable $f$ (define $f = 0$ on $E$), giving $\|f_n - f\|_\infty \to 0$.
<1>3. There is no smooth $h$ with $f \ast h = f$ for every $f \in L^1(I)$.
    Proof: on the circle, convolution with a fixed smooth $h$ maps $L^1$ into $C^\infty$ (each $f\ast h$ is smooth), and the operator $f \mapsto f\ast h$ is compact (it is the uniform limit of finite-rank operators — e.g. truncate the Fourier series of $h$; or use Ascoli--Arzel\`a on the image of the unit ball). The identity operator on $L^1$ is not compact (its image of the unit ball is the unit ball, not precompact). Hence $f\ast h \ne f$ for some $f$; equivalently an identity would have to be the Dirac $\delta_0$, which is not a function.
<1>4. Hölder's inequality: for $p, q \ge 1$ with $\frac1p + \frac1q = 1$, $\int|fg| \le \|f\|_p\|g\|_q$.
    Proof: the case $\|f\|_p = 0$ or $\|g\|_q = 0$ or $\|f\|_p = \infty$ or $\|g\|_q = \infty$ is immediate. Otherwise normalize $\|f\|_p = \|g\|_q = 1$. The given inequality $ab \le \frac{a^p}{p} + \frac{b^q}{q}$ with $a = |f(x)|$, $b = |g(x)|$ yields $|f(x)g(x)| \le \frac{|f(x)|^p}{p} + \frac{|g(x)|^q}{q}$; integrating over $I$ gives $\int|fg| \le \frac1p + \frac1q = 1$. Scaling back ($f \leftarrow f/\|f\|_p$, $g \leftarrow g/\|g\|_q$) gives the claimed inequality.
<1>5. Young's inequality: for $1 \le p, q, r \le \infty$ with $\frac1p + \frac1q = 1 + \frac1r$, $\|f \ast g\|_r \le \|f\|_p\|g\|_q$.
    Proof: it suffices to treat $f, g \ge 0$ (replace $f, g$ by their absolute values; the bound below then shows the defining integral converges a.e. and in $L^r$). Assume first $1 \le p, q, r < \infty$ with $p < r$ and $q < r$; the remaining cases are the endpoints treated at the end. Write
    \[
    f(y)\,g(x-y) = \big(f(y)^p g(x-y)^q\big)^{1/r}\cdot f(y)^{1 - p/r}\cdot g(x-y)^{1 - q/r},
    \]
    which is an identity because the exponents of $f$ and of $g$ each add to $1$. Apply Hölder's inequality in the variable $y$ with the three exponents $r$, $s = \frac{p}{1 - p/r}$, and $t = \frac{q}{1 - q/r}$. These are conjugate: since $\frac1p + \frac1q = 1 + \frac1r$,
    \[
    \frac1r + \frac1s + \frac1t = \frac1r + \frac{1 - p/r}{p} + \frac{1 - q/r}{q} = \frac1p + \frac1q - \frac1r = 1.
    \]
    Moreover $s(1 - p/r) = p$ and $t(1 - q/r) = q$, so the three Hölder factors are
    \[
    \Big(\int f(y)^p g(x-y)^q\,dy\Big)^{1/r},\qquad \|f\|_p^{p/s} = \|f\|_p^{1 - p/r},\qquad \|g\|_q^{q/t} = \|g\|_q^{1 - q/r},
    \]
    giving pointwise
    \[
    |f \ast g(x)| \le \Big(\int f(y)^p g(x-y)^q\,dy\Big)^{1/r} \|f\|_p^{1 - p/r}\,\|g\|_q^{1 - q/r}.
    \]
    Raise both sides to the $r$-th power and integrate in $x$; Tonelli's theorem applies (all integrands are non-negative) and $\int_x g(x-y)^q\,dx = \|g\|_q^q$ for every $y$ (translation invariance), so
    \[
    \|f \ast g\|_r^r \le \|f\|_p^{r-p}\,\|g\|_q^{r-q}\, \int\!\!\int f(y)^p g(x-y)^q\,dy\,dx = \|f\|_p^{r-p}\,\|g\|_q^{r-q}\,\|f\|_p^p\,\|g\|_q^q = \|f\|_p^r\,\|g\|_q^r,
    \]
    and taking $r$-th roots yields $\|f \ast g\|_r \le \|f\|_p\|g\|_q$.
    The endpoint cases: if $r = \infty$ then $\frac1p + \frac1q = 1$ and Hölder gives $|f \ast g(x)| \le \|f\|_p\|g\|_q$ for every $x$; if $q = 1$ then $r = p$ and Minkowski's inequality for integrals gives $\|f \ast g\|_p \le \int\|f(\cdot - y)\|_p|g(y)|\,dy = \|f\|_p\|g\|_1$; the case $p = 1$ is symmetric; and $r = 1$ forces $p = q = 1$, which is Tonelli. (If $p \ge r$ in the finite case, then $1/q = 1 + 1/r - 1/p \ge 1$, forcing $q = 1$ and $p = r$, so the finite cases with $p < r, q < r$ together with the endpoints are exhaustive.)

<1>6. Q.E.D.
:::
