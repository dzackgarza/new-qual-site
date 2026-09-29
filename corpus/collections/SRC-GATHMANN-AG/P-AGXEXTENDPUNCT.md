---
schema: qual/card@1
id: P-AGXEXTENDPUNCT
kind: problem
title: Regular functions on the punctured affine plane extend across the puncture
classification:
  areas:
  - algebraic-geometry
  topics:
  - Regular Functions
  - Hartogs Extension
  - Affine Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the current Problem Set 3, Problem 5 card and its recorded Gathmann
    collection context, together with the retained migration comparison that
    records the source wording defect already corrected by the erratum below.
    No source solution is incorporated. Independently cross-checked the
    extension argument against the equivalent punctured-plane calculation on
    Hartshorne I.3.6 (P-AGH36PUNCTPLANE).
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the complete proof and checked the principal-open cover
    U=D(x) union D(y), equality of the two localization representatives in
    k(x,y), and the UFD divisibility step. Coprimality of x and y forces
    x^m|a and y^n|b, so the representatives are one polynomial; uniqueness
    follows because the punctured plane is a nonempty open subset of the
    irreducible affine plane.
---

::: {.problem}
Let $U \da \AA^2 \sm \ts{(0, 0)}$, an open subset of $\AA^2$.
Prove that any regular function on $U$ extends to a regular function on all of $\AA^2$.
:::

::: {.solution}
Let $k$ be the ground field and put
$$
R=k[x,y].
$$
Then
$$
U=D(x)\cup D(y).
$$

::: pf

::: {.pf-step #representation-on-principal-opens}
A regular function $f\in\OO(U)$ is represented on the two principal
opens by
$$
f|_{D(x)}=\frac{a}{x^m},
\qquad
f|_{D(y)}=\frac{b}{y^n}
$$
for some $a,b\in R$ and $m,n\ge0$.

::: pf-proof
The principal opens are affine:
$$
D(x)=\Spec R_x,
\qquad
D(y)=\Spec R_y.
$$
Hence
$$
\OO(D(x))=R_x,
\qquad
\OO(D(y))=R_y.
$$
Every element of these localizations has the displayed form.
:::

:::

::: {.pf-step #representatives-agree-on-overlap}
The two representatives in step [](#representation-on-principal-opens){.pf-ref} are restrictions of one
polynomial $c\in k[x,y]$.

::: pf-proof
On the overlap
$$
D(xy)=D(x)\cap D(y)
$$
the two representatives agree. Since $R$ is a domain, equality in
$R_{xy}\subseteq k(x,y)$ gives
$$
\frac{a}{x^m}
=
\frac{b}{y^n},
$$
hence
$$
ay^n=bx^m.
$$

The ring $R=k[x,y]$ is a UFD, and $x$ and $y$ are relatively prime prime
elements. Therefore $x^m\mid ay^n$ implies
$$
x^m\mid a,
$$
and similarly $y^n\mid b$. Write
$$
a=x^m c,
\qquad
b=y^n c'
$$
with $c,c'\in R$. Substitution into $ay^n=bx^m$ gives
$$
c=c'.
$$
Thus
$$
f|_{D(x)}=c=f|_{D(y)}.
$$
Since $D(x)$ and $D(y)$ cover $U$, the function $f$ is the restriction of
the polynomial $c$ to all of $U$.
:::

:::

::: {.pf-step #extension-exists-and-unique}
Every regular function on $U$ extends uniquely to a regular
function on $\AA^2$.

::: pf-proof
By step [](#representatives-agree-on-overlap){.pf-ref}, a given $f\in\OO(U)$ is the restriction of some
$$
c\in k[x,y]=\OO(\AA^2),
$$
so $c$ is the required extension.

If two polynomials extend the same $f$, their difference vanishes on the
nonempty open subset $U$ of the irreducible variety $\AA^2$. Hence their
difference is the zero polynomial. The extension is therefore unique.
:::

:::

::: pf-qed
Step [](#extension-exists-and-unique){.pf-ref} is exactly the required extension statement, based on the
localization calculation in steps [](#representation-on-principal-opens){.pf-ref} and [](#representatives-agree-on-overlap){.pf-ref}.
:::

:::
:::

::: {.remark}
Erratum: the source asks about "a set $U$ in the complement of $(0,0)$".
The statement needs $U$ to be the whole complement: on the open set $D(x) \subseteq \AA^2 \sm \ts{(0,0)}$ the regular function $1/x$ does not extend to $\AA^2$.
:::
