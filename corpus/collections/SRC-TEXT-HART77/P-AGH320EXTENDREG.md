---
schema: qual/card@1
id: P-AGH320EXTENDREG
kind: problem
title: Extending a regular function across a normal point in dimension at least two
classification:
  areas:
  - algebraic-geometry
  topics:
  - Regular Functions
  - Normal Varieties
  - Dimension
relations:
- kind: uses
  target: P-AGH317NORMAL
- kind: uses
  target: P-AGH312DIMLOCAL
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts with Hartshorne I.3.20 and restored the source reference to III.3.5. The intended algebraic input is the height-one intersection theorem for Noetherian normal domains.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the reduction to the normal local ring at P, the membership in every height-one localization, and the punctured affine-line counterexample against Matsumura, Commutative Ring Theory, Theorem 11.5, and independent Hartshorne solution notes.'
---

::: {.problem}
Let $Y$ be a variety of dimension $\geq 2$, let $P \in Y$ be a normal point, and let $f$ be a regular function on $Y \sm \ts{P}$.

(a) Show that $f$ extends to a regular function on $Y$.

(b) Show that this would be false for $\dim Y = 1$. See (III, Ex. 3.5) for a generalization.
:::

::: {.solution}
Let
$$
K=K(Y)
$$
be the function field of $Y$.
Since $Y\setminus\{P\}$ is a nonempty open subset, the given regular function determines an element, again denoted $f$, of $K$.

<1>1. Put
$$
R=\mco_{P,Y}.
$$
Then $R$ is a Noetherian normal local domain of dimension at least two.

::: {.proof}
Local rings of varieties are Noetherian domains.
The hypothesis that $P$ is normal says exactly that $R$ is integrally closed in its fraction field, so $R$ is normal.
By [[P-AGH312DIMLOCAL]],
$$
\dim R=\dim Y\ge2.
$$
Its fraction field is $K(Y)=K$.
:::

<1>2. For every height-one prime $\mathfrak q\subset R$, the rational function $f$ belongs to $R_{\mathfrak q}$.

::: {.proof}
Choose an affine open neighborhood $U\subseteq Y$ of $P$, write
$$
A=A(U),
\qquad
\mathfrak m=I_U(P),
$$
so that $R=A_{\mathfrak m}$.
The prime $\mathfrak q$ has the form
$$
\mathfrak q=\mathfrak p A_{\mathfrak m}
$$
for a prime $\mathfrak p\subsetneq\mathfrak m$.
The strict containment follows because $\operatorname{ht}\mathfrak q=1$ whereas
$$
\operatorname{ht}\mathfrak m=\dim R\ge2.
$$

The irreducible closed set $V(\mathfrak p)\subseteq U$ therefore contains a closed point $Q\ne P$.
The function $f$ is regular at $Q$.
Hence, after shrinking inside the affine variety $U$, it has a representation
$$
f=\frac{a}{b}
$$
with $a,b\in A$ and $b(Q)\ne0$.
Because $Q\in V(\mathfrak p)$, the inequality $b(Q)\ne0$ implies
$$
b\notin\mathfrak p.
$$
Thus $f\in A_{\mathfrak p}$.
Since $\mathfrak p\subseteq\mathfrak m$,
$$
A_{\mathfrak p}\cong (A_{\mathfrak m})_{\mathfrak pA_{\mathfrak m}}
=R_{\mathfrak q},
$$
which proves the claim.
:::

<1>3. The rational function $f$ belongs to $R=\mco_{P,Y}$.

::: {.proof}
For a Noetherian normal domain, the height-one intersection theorem states that, inside its fraction field,
$$
R=\bigcap_{\operatorname{ht}\mathfrak q=1}R_{\mathfrak q}.
$$
This is Matsumura, *Commutative Ring Theory*, Theorem 11.5.
Step <1>2 places $f$ in every ring in this intersection, so $f\in R$.
:::

<1>4. The function $f$ extends to a regular function on all of $Y$, proving (a).

::: {.proof}
By step <1>3, the germ $f\in\mco_{P,Y}$ is represented by a regular function $g$ on some open neighborhood $V$ of $P$.
Both $g$ and the original function on $Y\setminus\{P\}$ represent the same element of $K(Y)$.
Hence they agree on the overlap
$$
V\setminus\{P\}.
$$
They therefore glue to a regular function on
$$
V\cup(Y\setminus\{P\})=Y
$$
extending the original $f$.
:::

<1>5. The assertion fails in dimension one.

::: {.proof}
Take
$$
Y=\AA^1,
\qquad
P=0,
$$
and on $Y\setminus\{0\}=D(x)$ take
$$
f=\frac1x.
$$
This is regular on $D(x)$.
If it extended regularly across the origin, its germ there would lie in
$$
\mco_{0,\AA^1}=k[x]_{(x)}.
$$
But $1/x$ does not belong to this localization: every denominator of an element of $k[x]_{(x)}$ is nonzero at $x=0$, whereas a representation of $1/x$ in reduced form has denominator divisible by $x$.
Indeed, if
$$
\frac1x=\frac{a}{s}
$$
with $a,s\in k[x]$ and $s\notin(x)$, then $s=ax$, so $s(0)=0$, contradicting $s\notin(x)$.
Thus no extension exists, proving (b).
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove (a), and step <1>5 proves (b).
:::
:::
