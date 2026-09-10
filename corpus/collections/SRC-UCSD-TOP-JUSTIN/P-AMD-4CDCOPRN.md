---
schema: qual/card@1
id: P-AMD-4CDCOPRN
kind: problem
title: Homology of the mapping torus of a degree-$d$ map $S^n\to S^n$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $X = S^n\cross I$ with its ends glued together by a map $S^n \circlearrowleft$ of degree $d$, calculate $H_*(X)$.
:::

::: {.solution}
Let $M_f$ denote the mapping torus of $f:S^n\to S^n$.

<1>1. For $n\ge1$, the Wang exact sequence of the mapping torus contains
$$
\cdots\to H_k(S^n)\xrightarrow{1-f_*}H_k(S^n)
\to H_k(M_f)\to H_{k-1}(S^n)\xrightarrow{1-f_*}H_{k-1}(S^n)\to\cdots.
$$
::: {.proof}
This is the Mayer--Vietoris sequence for a cover of the base circle by two arcs, after identifying the two components of the overlap. The difference between the two gluing maps is $1-f_*$, yielding the displayed Wang sequence.
:::

<1>2. On $H_n(S^n)\cong\mathbb Z$, the map $1-f_*$ is multiplication by $1-d$, while on $H_0(S^n)\cong\mathbb Z$ it is zero.
::: {.proof}
By definition of degree, $f_*$ acts by multiplication by $d$ on $H_n(S^n)$. Since $S^n$ is connected for $n\ge1$, every self-map induces the identity on $H_0$.
:::

<1>3. If $n\ge2$, then
$$
\boxed{
H_k(M_f;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,1,\\
\mathbb Z/(1-d),&k=n,\\
\mathbb Z,&k=n+1\text{ and }d=1,\\
0,&\text{otherwise},
\end{cases}}
$$
where $\mathbb Z/(0)=\mathbb Z$.
::: {.proof}
For degrees $n,n+1$, exactness gives
$$
0\to H_{n+1}(M_f)\to\mathbb Z\xrightarrow{1-d}\mathbb Z\to H_n(M_f)\to0.
$$
Thus $H_{n+1}=\ker(1-d)$ and $H_n=\operatorname{coker}(1-d)$. Around degree $1$, the zero map $1-f_*:H_0(S^n)\to H_0(S^n)$ gives $H_1(M_f)\cong\mathbb Z$. All intermediate groups vanish because $S^n$ has no homology in degrees $1,\dots,n-1$.
:::

<1>4. If $n=1$, then
$$
\boxed{
H_0(M_f)=\mathbb Z,\qquad
H_1(M_f)\cong\mathbb Z\oplus\mathbb Z/(1-d),\qquad
H_2(M_f)=\ker(1-d),
}
$$
and higher homology vanishes.
::: {.proof}
The Wang sequence gives
$$
0\to H_2(M_f)\to\mathbb Z\xrightarrow{1-d}\mathbb Z
\to H_1(M_f)\to\mathbb Z\xrightarrow{0}\mathbb Z\to H_0(M_f)\to0.
$$
Hence $H_2=\ker(1-d)$ and there is a short exact sequence
$$
0\to\mathbb Z/(1-d)\to H_1(M_f)\to\mathbb Z\to0.
$$
It splits because $\mathbb Z$ is free.
:::

<1>5. If one also allows $n=0$, the four self-maps of $S^0$ have reduced degrees $1,-1,0,0$. For degree $1$ the mapping torus is $S^1\sqcup S^1$; for degree $-1$ it is $S^1$; and for either degree-$0$ constant map it is a circle with a contractible interval attached. Thus
$$
(d=1):\quad H_0=H_1=\mathbb Z^2,
$$
while
$$
(d=-1\text{ or }0):\quad H_0=H_1=\mathbb Z,
$$
with all higher groups zero.
::: {.proof}
For $S^0=\{a,b\}$, the mapping torus is obtained from two intervals by identifying each top endpoint with the image under $f$ at the bottom. The identity closes both intervals separately; the transposition joins them into one circle; a constant map closes one interval into a circle and attaches the other interval as a tree edge.
:::
:::
