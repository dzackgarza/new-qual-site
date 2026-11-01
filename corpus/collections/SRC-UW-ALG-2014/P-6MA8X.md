---
schema: qual/card@1
id: P-6MA8X
kind: problem
title: $\Tor$ against $R/(x)$, flatness via $\Tor_1$, and finitely generated flat modules over a PID are free
classification:
  areas:
  - algebra
  topics:
  - Homological Algebra
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2014`; it is the standard Tor and
    flatness statement and no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    (a) the two-term free resolution $0\to R\xrightarrow{x}R\to R/(x)\to0$ is available because $x$ is
    a nonzero divisor, giving $\Tor_0=M/xM$, $\Tor_1=M[x]$ and $\Tor_i=0$ for $i\ge2$. (b) both
    directions from the long exact sequence of Tor and exactness of $-\otimes M$. (c) flat implies
    torsion-free by exactness of $-\otimes M$ applied to $0\to R\xrightarrow{a}R$, and finitely
    generated torsion-free over a PID is free by the structure theorem. Nothing is left in outline.
---

::: {.problem}
Let $R$ be a commutative ring and let $M$ be an $R$-module.

(a) Let $x\in R$ be a nonzero divisor.
Compute $\Tor_i^R(R/(x),M)$ for $i\geq 0$.

(b) Show that $M$ is a flat $R$-module if and only if $\Tor_1^R(M,N)=0$ for all $R$-modules $N$.

(c) Conclude that if $R$ is a PID and $M$ is a finitely generated $R$-module, then $M$ is flat if and only if $M$ is free.
:::

::: {.solution}

Let $R$ be a commutative ring, $M$ an $R$-module, and $\Tor_i=\Tor_i^R$.

::: pf

::: {.pf-step #s1}

Part (a): if $x\in R$ is a nonzero divisor then
$$
\Tor_0(R/(x),M)=M/xM,\qquad \Tor_1(R/(x),M)=M[x]=\{m\in M:xm=0\},\qquad \Tor_i(R/(x),M)=0\ \ (i\ge2).
$$

::: pf-proof

Since $x$ is a nonzero divisor, multiplication by $x$ is injective and
$$
0\longrightarrow R\xrightarrow{\ x\ }R\longrightarrow R/(x)\longrightarrow0
$$
is a free resolution of $R/(x)$ (the quotient map kills $xR$, whose kernel is $xR$ because $x$ is injective). Applying $-\otimes_RM$ gives the complex
$$
0\longrightarrow M\xrightarrow{\ x\ }M\longrightarrow0,
$$
placed in degrees $1,0$. Its homology is $\Tor_i$. In degree $0$ this is $\operatorname{coker}(x\cdot)=M/xM$; in degree $1$ it is $\ker(x\cdot)=M[x]$; in all other degrees the complex is $0$, so $\Tor_i=0$ for $i\ge2$.

:::

:::

::: {.pf-step #s2}

Part (b): $M$ is flat if and only if $\Tor_1(M,N)=0$ for every $R$-module $N$.

::: pf-proof

If $M$ is flat then $-\otimes_RM$ is exact, so it has no higher derived functors and $\Tor_i(M,N)=0$ for $i\ge1$ and all $N$.

Conversely, suppose $\Tor_1(M,N)=0$ for all $N$; we must show that $-\otimes_RM$ carries injections to injections. Let $0\to A\to B$ be exact and put $C=B/A$, so that $0\to A\to B\to C\to0$ is exact. The long exact sequence of $\Tor_\bullet(M,-)$ for this short exact sequence ends
$$
\Tor_1(M,C)\longrightarrow A\otimes_RM\longrightarrow B\otimes_RM\longrightarrow C\otimes_RM\longrightarrow0 .
$$
The first term vanishes by hypothesis, so $0\to A\otimes_RM\to B\otimes_RM$ is exact. Hence $-\otimes_RM$ preserves injections, which is flatness.

:::

:::

::: {.pf-step #s3}

Part (c): if $R$ is a PID and $M$ finitely generated, then $M$ is flat if and only if $M$ is free.

::: pf-proof

A free module is projective, hence flat.

Conversely let $M$ be flat and let $0\ne a\in R$. Since $R$ is a domain, $a$ is a nonzero divisor, so $0\to R\xrightarrow{a}R\to R/(a)\to0$ is exact; by flatness,
$$
0\longrightarrow M\xrightarrow{\ a\ }M\longrightarrow R/(a)\otimes_RM\longrightarrow0
$$
is exact, so multiplication by $a$ is injective on $M$. Hence $M$ has no nonzero element killed by a nonzero scalar, that is, $M$ is torsion-free.

A finitely generated torsion-free module over a PID is free: by the structure theorem, $M\cong R^r\oplus R/(a_1)\oplus\cdots\oplus R/(a_k)$ with $a_j\ne0$ nonunits, and if $k\ge1$ then $R/(a_1)$ has $a_1$-torsion, contradicting torsion-freeness. So $k=0$ and $M\cong R^r$.

(Equivalently, in the notation of (a): for a nonunit $a\ne0$, $\Tor_1(R/(a),M)=M[a]=0$ by (a) and (b), which is the same conclusion.)

:::

:::

:::

:::
