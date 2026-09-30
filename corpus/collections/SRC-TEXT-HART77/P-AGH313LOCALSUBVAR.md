---
schema: qual/card@1
id: P-AGH313LOCALSUBVAR
kind: problem
title: The local ring of a subvariety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Local Rings
  - Subvarieties
  - Function Fields
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the full construction and all three requested conclusions with Hartshorne I.3.13. After shrinking around a point of Y, the proof identifies the ring with A(X) localized at the prime ideal of Y.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the localization identification, residue-field computation, and codimension formula against independent published solutions. The reduction preserves both dimensions because the chosen intersections with X and Y are nonempty open subsets.'
---

::: {.problem}
Let $Y \subseteq X$ be a subvariety.
Let $\mco_{Y,X}$ be the set of equivalence classes $\generators{U, f}$ where $U \subseteq X$ is open, $U \intersect Y \neq \emptyset$, and $f$ is a regular function on $U$; two classes $\generators{U,f}$ and $\generators{V,g}$ are equivalent if $f = g$ on $U \intersect V$.

Show that $\mco_{Y,X}$ is a local ring with residue field $K(Y)$ and dimension $\dim X - \dim Y$.
It is called the **local ring of $Y$ on $X$**. When $Y = P$ is a point this recovers $\mco_P$, and when $Y = X$ it recovers $K(X)$.
Note also that if $Y$ is not a point then $K(Y)$ is not algebraically closed, so this construction produces local rings whose residue fields are not algebraically closed.
:::

::: {.solution}
Choose a point $P\in Y$.
Since $Y$ is locally closed in $X$, there is an open neighborhood $W\subseteq X$ of $P$ such that $Y\cap W$ is closed in $W$; shrinking further, take $W$ affine.

::: pf

::: pf-step

Replacing $(X,Y)$ by $(W,Y\cap W)$ does not change $\mco_{Y,X}$, $\dim X$, or $\dim Y$.

::: pf-proof

Both $W\cap Y$ and the intersection of $Y$ with the domain of any representative $\generators{U,f}$ are nonempty open subsets of the irreducible variety $Y$.
Their intersection is therefore nonempty.
Thus restricting representatives from $U$ to $U\cap W$ defines a map
$$
\mco_{Y,X}\longrightarrow\mco_{Y\cap W,W},
$$
and regarding a representative on an open subset of $W$ as one on the same open subset of $X$ gives the inverse map.

Since $W$ is a nonempty open subset of the irreducible variety $X$ and $Y\cap W$ is a nonempty open subset of $Y$, their function fields agree with those of $X$ and $Y$, respectively.
Hence
$$
\dim W=\dim X,
\qquad
\dim(Y\cap W)=\dim Y.
$$
We may therefore assume from now on that $X$ is affine and that $Y$ is closed in $X$.

Put
$$
A=A(X),
\qquad
\mathfrak p=I(Y).
$$
The ideal $\mathfrak p$ is prime because $Y$ is irreducible.

:::

:::

::: {.pf-step #s2}

There is a canonical ring isomorphism
$$
\mco_{Y,X}\cong A_{\mathfrak p}.
$$

::: pf-proof

If $s\notin\mathfrak p$, then $s$ does not vanish identically on $Y$.
Hence the principal open set $D(s)$ meets $Y$, and the fraction $a/s$ is regular on $D(s)$.
This defines a homomorphism
$$
A_{\mathfrak p}\longrightarrow\mco_{Y,X},
\qquad
\frac{a}{s}\longmapsto\generators{D(s),a/s}.
$$
It is well-defined: if $a/s=b/t$ in $A_{\mathfrak p}$, then the two fractions agree in $K(X)$ and hence as regular functions on $D(st)$; this principal open meets $Y$ because $st\notin\mathfrak p$.

For surjectivity, let $\generators{U,f}$ be a class and choose $Q\in U\cap Y$.
Regularity of $f$ gives a principal open neighborhood $D(s)\subseteq U$ of $Q$ and an expression
$$
f=\frac{a}{s}
$$
on $D(s)$.
Since $s(Q)\ne0$ and $Q\in Y$, we have $s\notin\mathfrak p$.
The class $\generators{U,f}$ is therefore represented by the image of $a/s\in A_{\mathfrak p}$.

For injectivity, two fractions whose classes agree are equal as regular functions on a nonempty open subset of the irreducible affine variety $X$.
They are consequently equal in the function field $K(X)=\operatorname{Frac}A$, hence equal in the subring $A_{\mathfrak p}$.

:::

:::

::: {.pf-step #s3}

The ring $\mco_{Y,X}$ is local with residue field $K(Y)$.

::: pf-proof

By step [](#s2){.pf-ref}, it is the localization $A_{\mathfrak p}$, whose unique maximal ideal is
$$
\mathfrak pA_{\mathfrak p}.
$$
Its residue field is
$$
A_{\mathfrak p}/\mathfrak pA_{\mathfrak p}
\cong
(A/\mathfrak p)_{(A\setminus\mathfrak p)}.
$$
The image of $A\setminus\mathfrak p$ in the domain $A/\mathfrak p$ is exactly its set of nonzero elements.
Thus this localization is
$$
\operatorname{Frac}(A/\mathfrak p)=K(Y).
$$

:::

:::

::: {.pf-step #s4}

The dimension of the local ring is
$$
\dim\mco_{Y,X}=\boxed{\dim X-\dim Y}.
$$

::: pf-proof

The prime ideals of $A_{\mathfrak p}$ correspond to the prime ideals of $A$ contained in $\mathfrak p$, so
$$
\dim A_{\mathfrak p}=\operatorname{ht}\mathfrak p.
$$
For the finitely generated $k$-domain $A$, the affine dimension formula [@Har10a, Chapter I, §1] gives
$$
\operatorname{ht}\mathfrak p+\dim(A/\mathfrak p)=\dim A.
$$
Since $\dim A=\dim X$ and $\dim(A/\mathfrak p)=\dim Y$, step [](#s2){.pf-ref} gives the claimed equality.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves that $\mco_{Y,X}$ is local with residue field $K(Y)$, and step [](#s4){.pf-ref} computes its dimension.

:::

:::

:::
