---
schema: qual/card@1
id: E-HAT-3.A-8
kind: problem
title: "The Bockstein sequence of a Moore space is the Hom-Ext sequence"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-02
  note: >-
    Statement transcribed from the printed page -- printed page 320, rendered from
    tmp/hat/AT.pdf with pdftocairo at 200 dpi -- and compared with the text extraction at
    AT.txt:16006-16011; the two agree, including the displayed sequence. New card: exercises 7, 8
    and 9 of Section 3.A were uncarded.
- event: solution-written
  by: claude
  date: 2026-11-02
  note: >-
    Three steps: the coefficient sequence for a short exact sequence of abelian groups, from the
    short exact sequence of cochain complexes; the cohomology of a Moore space in degrees n and n+1
    as Hom and Ext; and the substitution into that sequence, including the case n = 1, where the
    term left of the printed sequence is H^0(X;C) and dies because H^0(X;B) surjects onto it.
---

::: {.problem}
Show that for a Moore space $M(G,n)$ the Bockstein long exact sequence in cohomology associated to the short exact sequence of coefficient groups $0\to A\to B\to C\to 0$ reduces to an exact sequence
$$
0\to\operatorname{Hom}(G,A)\to\operatorname{Hom}(G,B)\to\operatorname{Hom}(G,C)\to\operatorname{Ext}(G,A)\to\operatorname{Ext}(G,B)\to\operatorname{Ext}(G,C)\to 0.
$$

:::

::: {.solution}

::: pf

::: {.pf-step #bockstein}
For every space $X$ and every short exact sequence of abelian groups $0\to A\to B\to C\to0$ there is a long exact sequence
$$
\cdots\to H^{k}(X;A)\to H^{k}(X;B)\to H^{k}(X;C)\xrightarrow{\beta}H^{k+1}(X;A)\to H^{k+1}(X;B)\to\cdots
$$

::: pf-proof
The cochain complexes with coefficients in $A$, $B$ and $C$ form a short exact sequence
$$
0\to C^*(X;A)\to C^*(X;B)\to C^*(X;C)\to0,
$$
which is exact in each degree because $C^k(X;D)$ is a product of copies of $D$, one for each singular $k$-simplex, and a product of surjections of abelian groups is again surjective. The long exact homology sequence of a short exact sequence of cochain complexes is the displayed sequence, its connecting map being the Bockstein homomorphism $\beta$.

:::

:::

::: {.pf-step #moorecohomology}
For a Moore space $M(G,n)$ and any coefficient group $D$,
$$
H^n(M(G,n);D)\cong\operatorname{Hom}(G,D),\qquad H^{n+1}(M(G,n);D)\cong\operatorname{Ext}(G,D),
$$
while $H^k(M(G,n);D)=0$ for $k\notin\{0,n,n+1\}$.

::: pf-proof
The cellular chain complex of $M(G,n)$ is concentrated in degrees $0$, $n$ and $n+1$, with $H_0=\ZZ$, $H_n=G$ and no other homology. Universal coefficients gives $H^k=\operatorname{Hom}(H_k,D)\oplus\operatorname{Ext}(H_{k-1},D)$. At $k=n$ the two summands are $\operatorname{Hom}(G,D)$ and $\operatorname{Ext}(H_{n-1},D)=0$, since $H_{n-1}=0$ for $n\ge2$ and $H_0=\ZZ$ with $\operatorname{Ext}(\ZZ,D)=0$ for $n=1$. At $k=n+1$ they are $\operatorname{Hom}(H_{n+1},D)=0$ and $\operatorname{Ext}(G,D)$. For $k\notin\{0,n,n+1\}$ both adjacent groups vanish, except at $k=0$, which is $D$ and plays no part below.

:::

:::

::: {.pf-step #substitute}
Taking $X=M(G,n)$ and $k=n$ in step [](#bockstein){.pf-ref} and substituting step [](#moorecohomology){.pf-ref} gives the printed exact sequence.

::: pf-proof
The relevant stretch of the coefficient sequence is
$$
H^{n-1}(X;C)\xrightarrow{\beta}H^{n}(X;A)\to H^{n}(X;B)\to H^{n}(X;C)\xrightarrow{\beta}H^{n+1}(X;A)\to H^{n+1}(X;B)\to H^{n+1}(X;C)\to H^{n+2}(X;A),
$$
and $H^{n+2}(X;A)=0$ by step [](#moorecohomology){.pf-ref}, so substituting produces the printed six terms and exactness gives exactness at each of them from the second onwards. For $n\ge2$ the term $H^{n-1}(X;C)$ lies outside $\{0,n,n+1\}$ and vanishes, so the printed sequence also begins with $0$.

For $n=1$ that term is $H^0(X;C)=C$, and the connecting map $\beta\colon C\to H^1(X;A)=\operatorname{Hom}(G,A)$ has to vanish for the sequence to begin with $0$. It does: $H^0(X;B)\to H^0(X;C)$ is the map $B\to C$ on the groups of locally constant maps from the connected space $X$, hence is surjective, and exactness at $H^0(X;C)$ makes the following map zero. So the printed sequence is exact at its first term in this case as well.

:::

:::

:::

:::
