---
schema: qual/card@1
id: P-BDFPC
kind: problem
title: "1. Suppose $f \\colon [-1,1] \\to \\mathbb{R}$ is a bounded function"
classification:
  areas:
  - real-analysis
  topics:
  - riemann-integrability
  - integrals
  - stone-weierstrass
relations: []
review: draft
---
1.  Suppose $f \colon [-1,1] \to \mathbb{R}$ is a bounded function
that is continuous at $0$. Let $\alpha(x) = -1$ for
$x \in [-1,0]$ and $\alpha(x)=1$ for $x \in (0,1]$. Prove that
$f \in \mathcal{R}(\alpha)[-1,1]$, i.e., $f$ is Riemann
integrable with respect to $\alpha$ on $[-1,1]$, and
$\int_{-1}^1 f d\alpha = 2f(0)$.

2.  
Let $g \colon [0,1] \to \mathbb{R}$ be a continuous function
such that $\int_0^1 g(x)x^{3k+2} dx = 0$ for all
$k = 0, 1, 2, \ldots$. Prove that $g(x) =0$ for all
$x \in [0,1]$.

:::{.proof}
*Proof.* Let $\epsilon>0$. Choose $\delta >0$ so that if
$|x|<\delta$, then $|f(x)-f(0)|<\epsilon$. Let $P$ be a
partition of $[-1,1]$ with $0 \in P$ and
$\operatorname{mesh}(P)<\delta$. Then
$|U(f,P,\alpha)-L(f,P,\alpha)|=|\sum_{i=1}^n(M_i-m_i)\Delta \alpha_i|=(|\sup_{x \in [0,x_k]}f(x)-\inf_{x \in [0,x_k]}f(x)|)2<4\epsilon$.
Thus $f$ is integrable with respect to $\alpha$. Additionally,
we have $L(f,P,\alpha)\leq 2f(0)\leq U(f,P,\alpha)$ for all
partitions $P$ of the form described above, and so
$\int_{-1}^1 f d\alpha = 2f(0)$. ◻
:::

:::{.proof}
*Proof.* Since $g(x)$ is continuous, so is $g(x^{1/3})$. Thus by
the Weierstrauss Approximation Theorem, we can find a sequence
of polynomials $(p_n(x))\to g(x^{1/3})$ uniformly. Since this
holds for all values $x\in [0,1]$, we have that $(p_n(x^3))$
converges to $g(x)$ uniformly. Then we have $(x^2p_n(x^3))$
converges to $x^2g(x)$ uniformly. Note that by assumption,
$\int_0^1 g(x)x^2p_n(x^3)dx=0$, and so
$0 = \lim_{n \to \infty}\int_0^1 g(x)x^2p_n(x^3)dx=\int_0^1 \lim_{n \to \infty}g(x)x^2p_n(x^3)dx=\int_0^1x^2g^2(x)dx$.
Since $x^2g^2(x)$ is non-negative, and its integral is zero, we
conclude that $x^2g^2(x)=0$ for all $x$. Therefore, we have
$g(x)=0$. ◻
:::
::: {.solution}
> **AI-Generated Solution**

**Part 1.** For the step function $\alpha(x) = -1$ on $[-1,0]$ and $\alpha(x) = 1$ on $(0,1]$: $f \in \mathcal R(\alpha)[-1,1]$ and $\int_{-1}^1 f\,d\alpha = 2f(0)$.

<1>1. For any partition $P = \{-1 = x_0 < x_1 < \cdots < x_n = 1\}$ with $0 \in P$, $\Delta \alpha_i = \alpha(x_i) - \alpha(x_{i-1})$ is nonzero only for the subinterval containing $0$, where it equals $2$.
    Proof: $\alpha$ is constant ($-1$, resp. $1$) on both sides of $0$; the only jump is at $0$, of size $1 - (-1) = 2$.

<1>2. If $x_k = 0$, then $U(f, P, \alpha) - L(f, P, \alpha) = 2\,(M_k - m_k)$, where $M_k, m_k$ are the sup and inf of $f$ on $[x_{k-1}, x_k]$.
    Proof: by <1>1 the sums reduce to the single term $k$; $\Delta\alpha_k = 2$.

<1>3. Given $\eps > 0$, choose $\delta > 0$ with $|x| < \delta \Rightarrow |f(x) - f(0)| < \eps$ (continuity at $0$), and let $P$ be any partition with $0 \in P$ and $\mathrm{mesh}(P) < \delta$. Then $U(f,P,\alpha) - L(f,P,\alpha) \le 4\eps$.
    Proof: the subinterval containing $0$ lies inside $(-\delta, \delta)$, so $M_k - m_k \le 2\eps$; then <1>2 gives $U - L \le 4\eps$.

<1>4. $f \in \mathcal R(\alpha)[-1,1]$.
    Proof: <1>3 shows the Riemann–Stieltjes sums converge as $\mathrm{mesh}(P) \to 0$.

<1>5. $\int_{-1}^1 f\,d\alpha = 2f(0)$.
    Proof: with $0 \in P$, $L(f,P,\alpha) = 2\,m_k \le 2f(0) \le 2\,M_k = U(f,P,\alpha)$ (since $f(0) \in [m_k, M_k]$), and $U - L \to 0$; the common limit is $2f(0)$.

**Part 2.** If $g \in C([0,1])$ and $\int_0^1 g(x)\,x^{3k+2}\,dx = 0$ for all $k \ge 0$, then $g \equiv 0$.

<1>6. $\int_0^1 g(x)\,x^2 p(x^3)\,dx = 0$ for every polynomial $p$.
    Proof: $x^2 p(x^3)$ is a finite linear combination of powers $x^{3k+2}$, each of which integrates to $0$ against $g$.

<1>7. $\int_0^1 g(x)\,x^2 h(x^3)\,dx = 0$ for every $h \in C([0,1])$.
    <2>1. Polynomials $p_n$ converge to $h(x^{1/3})$ uniformly on $[0,1]$ (Weierstrass), so $p_n(x^3) \to h(x)$ uniformly.
        Proof: $x \mapsto h(x^{1/3})$ is continuous (composition of continuous maps); Weierstrass applies on the compact interval $[0,1]$.
    <2>2. $x^2 g(x)\,p_n(x^3) \to x^2 g(x)\,h(x)$ uniformly.
        Proof: $|x^2 g(x)| \le \|g\|_\infty$ is bounded, and <2>1 gives uniform convergence of the polynomial factor.
    <2>3. Q.E.D.
        Proof: $\int x^2 g\,p_n(x^3) = 0$ for all $n$ by <1>6; uniform convergence (<2>2) passes the limit under the integral.

<1>8. $g \equiv 0$.
    Proof: <1>7 with $h = g$ gives $\int_0^1 x^2 g(x)^2\,dx = 0$; the integrand $x^2 g(x)^2 \ge 0$ is continuous, hence identically $0$, so $g = 0$ on $(0,1]$ and by continuity at $0$ as well.
:::
