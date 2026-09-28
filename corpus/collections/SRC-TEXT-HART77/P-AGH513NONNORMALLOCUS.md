---
schema: qual/card@1
id: P-AGH513NONNORMALLOCUS
kind: problem
title: The nonnormal locus of a variety is a proper closed subset
classification:
  areas:
  - algebraic-geometry
  topics:
  - Normal Varieties
  - Integral Closure
  - Local Rings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the requested direct proof and the finiteness-of-integral-closure hint with the retained Hartshorne I.5.13 transcription. The proof identifies the nonnormal locus on each affine chart with the support of the finite module Abar/A, using localization of normalization, and observes that this support omits the generic point.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
It is a fact that any regular local ring is an integrally closed domain.
Thus every variety has a nonempty open subset of normal points.

In this exercise, show directly, without using the regularity fact, that the set of nonnormal points of a variety is a proper closed subset.
You will need the finiteness of integral closure.
:::

::: {.solution}
Let $X$ be a variety with function field $K=k(X)$.
Normality is local, so we first work on an affine open
$$
U=\Spec A\subseteq X,
$$
where $A$ is a finitely generated $k$-domain with fraction field $K$.
Let $\overline A$ denote the integral closure of $A$ in $K$.

<1>1. The $A$-module
$$
M=\overline A/A
$$
is finite.

::: {.proof}
The finiteness theorem for normalization says that the integral closure of a finitely generated domain over a field in its finite fraction-field extension is finite as a module over the original ring [@Har10a, Theorem I.3.9A]. Here the extension of fraction fields is the identity $K/K$, so $\overline A$ is a finite $A$-module.
Its quotient $M$ is therefore finite as well.
:::

<1>2. For a prime $\mathfrak p\in\Spec A$, the local ring $A_{\mathfrak p}$ is normal if and only if
$$
M_{\mathfrak p}=0.
$$

::: {.proof}
Integral closure commutes with localization:
$$
\overline{A_{\mathfrak p}}
=
(\overline A)_{\mathfrak p}
\subseteq K.
$$
Indeed, localization of an integral extension is integral.
Conversely, if $u\in K$ is integral over $A_{\mathfrak p}$, choose one denominator $s\notin\mathfrak p$ containing all denominators in a monic equation for $u$.
For a sufficiently large $N$, multiplying that equation after setting $v=s^Nu$ gives a monic equation for $v$ with coefficients in $A$.
Thus $v\in\overline A$ and
$$
u=v/s^N\in(\overline A)_{\mathfrak p}.
$$
Thus $(\overline A)_{\mathfrak p}$ is exactly the integral closure of $A_{\mathfrak p}$ in its fraction field.

Consequently
$$
A_{\mathfrak p}\text{ is integrally closed}
\quad\Longleftrightarrow\quad
A_{\mathfrak p}=(\overline A)_{\mathfrak p}.
$$
The localized exact sequence
$$
0\longrightarrow A_{\mathfrak p}
\longrightarrow(\overline A)_{\mathfrak p}
\longrightarrow M_{\mathfrak p}
\longrightarrow0
$$
shows that this equality is equivalent to $M_{\mathfrak p}=0$.
Since $A_{\mathfrak p}$ is already a domain, integrally closed is exactly normality here.
:::

<1>3. The nonnormal locus in $U$ is the closed subset
$$
\boxed{\operatorname{NNor}(U)
=
\operatorname{Supp}_A(M)
=
V(\Ann_A M).}
$$

::: {.proof}
By step <1>2, a prime $\mathfrak p$ is nonnormal exactly when the localization $M_{\mathfrak p}$ is nonzero.
This is the definition of the support of the finite module $M$.
For a finite module over a ring,
$$
\operatorname{Supp}_A(M)=V(\Ann_A M).
$$
Indeed, if generators $m_1,\ldots,m_s$ all vanish after localization at $\mathfrak p$, choose denominators outside $\mathfrak p$ killing them and multiply those denominators to obtain an element of $\Ann_A M$ outside $\mathfrak p$.
The converse is immediate.
Thus the nonnormal locus on $U$ is closed.
:::

<1>4. This closed subset is proper.

::: {.proof}
Let $\eta$ be the generic point of $U$, corresponding to the zero prime.
Its local ring is the fraction field
$$
A_{(0)}=K,
$$
which is integrally closed in itself.
By step <1>2,
$$
M_{(0)}=0.
$$
Thus $\eta\notin\operatorname{Supp} M$.
Since the support is closed and omits the generic point of the irreducible space $U$, it is a proper closed subset.
Equivalently, $\Ann_A M$ contains a nonzero element, and the principal open defined by that element consists entirely of normal points.
:::

<1>5. The nonnormal locus of $X$ is a proper closed subset of $X$.

::: {.proof}
Choose a finite affine open cover
$$
X=U_1\cup\cdots\cup U_N.
$$
Normality of a local ring is unchanged when computed in an open neighborhood, so the global nonnormal locus $N$ satisfies
$$
N\cap U_i=\operatorname{NNor}(U_i).
$$
Step <1>3 makes each intersection closed in $U_i$.
Closedness is local on an open cover, hence $N$ is closed in $X$.

The generic point of the irreducible variety $X$ has local ring $K$, a field, and is therefore normal.
Thus it does not lie in $N$.
Hence $N$ is proper.
Its complement is the nonempty open normal locus.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 give the finite-module description and proper closedness on every affine chart, and step <1>5 glues those descriptions on the variety.
:::
:::
