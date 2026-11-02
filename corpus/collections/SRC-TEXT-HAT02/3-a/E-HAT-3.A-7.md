---
schema: qual/card@1
id: E-HAT-3.A-7
kind: problem
title: "Moore spaces of a short exact sequence, and a six-term Hom-Ext sequence"
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
    AT.txt:16000-16005; the two agree, including the displayed sequence. The card is new: Hatcher's
    Section 3.A prints nine exercises and the collection held cards only for exercises 1-6, so
    exercises 7, 8 and 9 were uncarded before this pass.
- event: solution-written
  by: claude
  date: 2026-11-02
  note: >-
    Four steps: Moore spaces are constructed from a free presentation; the quotient of two models
    along a realisation of the inclusion is shown by the long exact homology sequence to be a Moore
    space for the cokernel; universal coefficients identifies the cohomology of the pair and of each
    model with Hom and Ext; the long exact cohomology sequence of the pair then gives the printed
    six-term sequence. The only outside results used are Proposition 2.22 (a good pair's quotient
    computes relative homology) and universal coefficients, both cited.
---

::: {.problem}
Show that for a short exact sequence of abelian groups $0\to A\to B\to C\to 0$, a Moore space $M(C,n)$ can be realized as a quotient $M(B,n)/M(A,n)$.

Applying the long exact sequence of cohomology for the pair $(M(B,n),M(A,n))$ with any coefficient group $G$, deduce an exact sequence
$$
0\to\operatorname{Hom}(C,G)\to\operatorname{Hom}(B,G)\to\operatorname{Hom}(A,G)\to\operatorname{Ext}(C,G)\to\operatorname{Ext}(B,G)\to\operatorname{Ext}(A,G)\to 0.
$$

:::

::: {.solution}

::: pf

::: {.pf-step #moore}
For every abelian group $H$ and every $n\ge 1$ there is a CW complex $M(H,n)$ with a single $0$-cell, cells only in dimensions $n$ and $n+1$, and $\widetilde H_n(M(H,n))=H$, $\widetilde H_k(M(H,n))=0$ for $k\ne n$.

::: pf-proof
Take a free presentation $0\to K\to F\to H\to0$ with $F$ free on a set $S$ and $K$ free on a set $T$; both bases exist because a subgroup of a free abelian group is free. Let
$$
M(H,n)=\bigvee_{s\in S}S^n\cup\bigcup_{t\in T}e^{n+1}_t,
$$
attaching $e^{n+1}_t$ along a map $S^n\to\bigvee_{s\in S}S^n$ whose class in $\pi_n(\bigvee_{s\in S}S^n)=F$ is the basis element $t$. Then $C_0=\ZZ$, $C_n=\ZZ[S]$, $C_{n+1}=\ZZ[T]$ and every other cellular chain group vanishes, while the boundary $C_{n+1}\to C_n$ is exactly the presentation map $K\to F$. Hence $H_{n+1}=\ker(K\to F)=0$ by injectivity, $H_n=\operatorname{coker}(K\to F)=H$, $H_0=\ZZ$, and $H_k=0$ for the remaining $k$ because both adjacent chain groups vanish there.

:::

:::

::: {.pf-step #quotient}
Let $0\to A\xrightarrow{\alpha}B\xrightarrow{\beta}C\to0$ be exact. For any choice of the two models, the cofibre of a cellular map realizing $\alpha$ is a Moore space for $C$; in particular $M(C,n)$ is realized as such a quotient.

::: pf-proof
By the cellular approximation theorem a map realizing $\alpha$ is homotopic to a cellular map $f\colon M(A,n)\to M(B,n)$, and replacing $f$ by its mapping cylinder does not change the cofibre up to homotopy while making $M(A,n)$ a subcomplex of a CW complex homotopy equivalent to $M(B,n)$. So there is a CW pair $(X,A')$ with a homotopy equivalence of pairs to $(M(B,n),M(A,n))$, and its quotient $Q=X/A'$ has $Q\simeq M(B,n)/M(A,n)$.

The pair is a good pair, so $H_k(Q)\cong H_k(X,A')$ (Hatcher, Proposition 2.22). The long exact homology sequence of the pair, with $H_k(A')=0$ for $k\ne n$, gives $H_k(Q)=0$ for $k\ne n$: for $k\notin\{n,n+1\}$ both groups $H_k(A')$ and $H_k(X)$ vanish, and for $k=n+1$ the sequence reads $0=H_{n+1}(A')\to H_{n+1}(X)=0\to H_{n+1}(Q)\to H_n(A')=A\xrightarrow{\alpha}B$, so $H_{n+1}(Q)=0$ because $\alpha$ is injective. At $k=n$ it reads $A\xrightarrow{\alpha}B\to H_n(Q)\to H_{n-1}(A')=0$, so $H_n(Q)=\operatorname{coker}\alpha=C$. Thus $Q$ has the homology of a Moore space for $C$, and being a CW complex it is one.

:::

:::

::: {.pf-step #paircohomology}
For every coefficient group $G$, writing $X$ for a model of $M(B,n)$ and $A'$ for the subcomplex realizing $M(A,n)$,
$$
H^n(X,A';G)\cong\operatorname{Hom}(C,G),\quad H^{n+1}(X,A';G)\cong\operatorname{Ext}(C,G),
$$
and all other cohomology of the pair vanishes. Likewise $H^n(X;G)\cong\operatorname{Hom}(B,G)$, $H^{n+1}(X;G)\cong\operatorname{Ext}(B,G)$, $H^k(X;G)=0$ for $k\notin\{0,n,n+1\}$, and the same three statements with $A$ in place of $B$.

::: pf-proof
Universal coefficients for a pair reads
$$
0\to\operatorname{Ext}(H_{k-1}(X,A'),G)\to H^k(X,A';G)\to\operatorname{Hom}(H_k(X,A'),G)\to0.
$$
Since $H_*(X,A')$ is $C$ in degree $n$ and vanishes elsewhere, this gives $\operatorname{Hom}(C,G)$ at $k=n$, $\operatorname{Ext}(C,G)$ at $k=n+1$, and $0$ for every other $k$, both adjacent groups being zero there.

For the absolute case, $H_*(X)$ is $B$ in degree $n$ and $\ZZ$ in degree $0$ and vanishes elsewhere, so universal coefficients gives $H^n(X;G)=\operatorname{Hom}(B,G)\oplus\operatorname{Ext}(H_{n-1}(X),G)=\operatorname{Hom}(B,G)$ and $H^{n+1}(X;G)=\operatorname{Hom}(H_{n+1}(X),G)\oplus\operatorname{Ext}(B,G)=\operatorname{Ext}(B,G)$, with the outer group vanishing in each case. At $n=1$ the extra summands are $\operatorname{Ext}(H_0(X),G)=\operatorname{Ext}(\ZZ,G)=0$ and $\operatorname{Hom}(H_2(X),G)=0$, so the same two identifications hold. The statements for $A'$ are the same computation with $H_*(A')$ equal to $A$ in degree $n$.

:::

:::

::: {.pf-step #sequence}
The long exact cohomology sequence of the pair contains the printed six-term exact sequence.

::: pf-proof
The segment of that sequence spanning degrees $n$ and $n+1$ is
$$
H^n(X,A';G)\to H^n(X;G)\to H^n(A';G)\to H^{n+1}(X,A';G)\to H^{n+1}(X;G)\to H^{n+1}(A';G)\to H^{n+2}(X,A';G),
$$
and $H^{n+2}(X,A';G)=0$ by step [](#paircohomology){.pf-ref}. Substituting the identifications of that step gives
$$
\operatorname{Hom}(C,G)\to\operatorname{Hom}(B,G)\to\operatorname{Hom}(A,G)\to\operatorname{Ext}(C,G)\to\operatorname{Ext}(B,G)\to\operatorname{Ext}(A,G)\to0,
$$
which is exact at every term from $\operatorname{Hom}(B,G)$ onwards by exactness of the pair sequence. Exactness at the first term is not a property of the pair sequence: the map $\operatorname{Hom}(C,G)\to\operatorname{Hom}(B,G)$ is injective by left exactness of $\operatorname{Hom}$ applied to $0\to A\to B\to C\to0$. Prefixing it with $0$ therefore gives the printed sequence.

:::

:::

:::

:::
