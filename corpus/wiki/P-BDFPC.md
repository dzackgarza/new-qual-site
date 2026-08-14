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
