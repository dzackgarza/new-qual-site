---
schema: qual/card@1
id: P-EMAF1
kind: problem
title: Finite-field embeddings are characterized by divisibility of degrees
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked Fields 1 on PDF page 1; the printed inequality r<=s is insufficient and is replaced by divisibility, with embeddings distinguished from literal inclusion."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the degree obstruction, polynomial divisibility by iterated Frobenius, closure and exact size of the root subfield, and uniqueness of its presentation inside a common algebraic closure."
---

::: problem
Let $K$ and $L$ be finite fields.
Show that $K$ is isomorphic to a subfield of $L$ if and only if
$\#K=p^r$ and $\#L=p^s$ for the same prime $p$ and positive
integers $r,s$ with $r\mid s$.
:::

::: remark
The weaker inequality $r\leq s$ does not suffice:
$\mathbb F_4$ does not embed in $\mathbb F_8$, since
the tower law would require $2$ to divide $3$.
For abstract fields the criterion gives an embedding.
For fields inside one algebraic closure of $\mathbb F_p$,
it also characterizes literal containment.
:::

::: solution
<1>1. An embedding forces the stated characteristic and divisibility.

::: proof
Every finite field has prime characteristic $p$ and
is a finite-dimensional vector space over its prime
subfield $\mathbb F_p$ [@DF04]. Its size is therefore
$p^r$, where $r$ is that positive dimension.
An embedding preserves the identity and hence the
characteristic. Identify $K$ with its image in $L$.
If $d=[L:K]$, the tower law gives
$$
s=[L:\mathbb F_p]=[L:K][K:\mathbb F_p]=dr.
$$
Consequently $r\mid s$. This also proves the
four-versus-eight obstruction in the remark.
:::

<1>2. If $r\mid s$, then $L$ contains a subfield of size $p^r$.

::: proof
Write $s=rd$ with $d\geq1$, and put
$h(T)=T^{p^r}-T$. In $\mathbb F_p[T]/(h)$ the
class $t$ satisfies $t^{p^r}=t$. Iterating this
identity $d$ times gives $t^{p^s}=t$. Hence
$h$ divides $T^{p^s}-T$ in $\mathbb F_p[T]$.

Lagrange's theorem in $L^\times$ shows that every
$a\in L$ satisfies $a^{p^s}=a$, including zero.
There are $p^s$ such elements, so the monic
polynomial of that degree factors as
$$
T^{p^s}-T=\prod_{a\in L}(T-a).
$$
Its divisor $h$ thus splits in $L$. Its derivative
is $-1$, so its roots are distinct and number
exactly $p^r$. Let $K'$ be their set.

It contains zero and one. The characteristic-$p$
binomial identity, iterated $r$ times, gives
$(a-b)^{p^r}=a^{p^r}-b^{p^r}$. Thus for $a,b\in K'$
the difference $a-b$ lies in $K'$. Multiplicativity
gives $(ab)^{p^r}=ab$, and for $a\ne0$ it gives
$(a^{-1})^{p^r}=a^{-1}$. Hence $K'$ is a subfield
of $L$, of the claimed cardinality.
:::

<1>3. The field $K$ embeds in this subfield $K'$.

::: proof
Every element of $K$ is a root of $h$, again by
Lagrange's theorem in $K^\times$. Thus $K$ is a
splitting field of $h$ over $\mathbb F_p$.
The field $K'$ is another: its elements are all
the roots. Uniqueness of splitting fields up to
base-field isomorphism gives $K\cong K'$ [@DF04].
Composing this isomorphism with $K'\subseteq L$
gives the required embedding.

Inside one algebraic closure, a field of size
$p^r$ is exactly the root set of $h$: it contains
$p^r$ roots and a degree-$p^r$ polynomial has no
others. Thus in that setting $K=K'$, which proves
the literal-containment assertion of the remark.
:::
:::
