---
schema: qual/card@1
id: P-JHUFA11AND
kind: problem
title: Unique normalized rotations of a simply connected bounded domain
classification:
  areas:
  - complex-analysis
  topics:
  - Automorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared September 2011 problem 4 on PDF page 22. Replaced the truncated title and removed the following Real Analysis heading and measure notation, which are outside this problem."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the hypotheses for the Riemann map, the conjugation derivative at the fixed point and uniqueness among all holomorphic self-maps, without assuming the competitor is an automorphism."
---

::: {.problem}
Let $U$ be a simply connected bounded domain in $\mathbb C$
and let $P\in U$. Prove that for every $t\in\mathbb R$
there is a unique holomorphic function $f:U\to U$
such that $f(P)=P$ and $f'(P)=e^{it}$.
:::

::: {.solution}
<1>1. A normalized Riemann map constructs the required function.

::: {.proof}
The domain $U$ is nonempty since it contains $P$, and
is a proper subset of $\mathbb C$ since it is bounded.
The Riemann mapping theorem gives a biholomorphism
$\phi:U\to D$, where $D$ is the unit disk, normalized
by $\phi(P)=0$ [[T-55MPA|Riemann mapping theorem]]. The normalization is obtained,
if necessary, by composing a Riemann map with a disk
automorphism sending the image of $P$ to zero.

For fixed $t\in\mathbb R$, put $\lambda=e^{it}$ and define
$$
f_t(z)=\phi^{-1}\bigl(\lambda\phi(z)\bigr).
$$
Rotation by $\lambda$ maps $D$ bijectively to itself,
so $f_t$ is a holomorphic automorphism of $U$ and
$f_t(P)=P$. Differentiating $\phi^{-1}\circ\phi$
at $P$ gives $(\phi^{-1})'(0)\phi'(P)=1$. Therefore
$$
f_t'(P)=(\phi^{-1})'(0)\lambda\phi'(P)=\lambda=e^{it}.
$$
This proves existence.
:::

<1>2. Every holomorphic self-map with the prescribed data equals $f_t$.

::: {.proof}
Let $f:U\to U$ be any holomorphic map satisfying those
data. Set $G=\phi\circ f\circ\phi^{-1}:D\to D$.
Then $G(0)=0$, and the chain rule gives
$$
G'(0)=\phi'(P)f'(P)(\phi^{-1})'(0)=e^{it}.
$$
The [[T-DAETF|Schwarz lemma]] yields $|G(w)|\leq|w|$. Thus
$H(w)=G(w)/w$ extends holomorphically across zero with
$H(0)=G'(0)=e^{it}$ and $|H|\leq1$ on $D$.
It attains modulus one at zero, so the maximum modulus
principle makes $H$ the constant $e^{it}$ [[T-BYNL5|maximum modulus principle]].
Hence $G(w)=e^{it}w$. Undoing the conjugation gives
$f(z)=\phi^{-1}(e^{it}\phi(z))=f_t(z)$, proving uniqueness.
:::

<1>3. Q.E.D.
::: {.proof}
Step <1>1 proves existence, and step <1>2 proves uniqueness.
:::
:::
