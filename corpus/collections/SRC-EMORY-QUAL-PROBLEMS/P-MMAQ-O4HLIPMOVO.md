---
schema: qual/card@1
id: P-MMAQ-O4HLIPMOVO
kind: problem
title: Finite-field embeddings and divisibility of extension degrees
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually verified the incorrect inequality r<=s in Fields 1 on PDF page 1; the existing solution instead proves divisibility."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Retained the valid divisibility proof, corrected its statement and conclusion to existence of an embedding, supplied the four-versus-eight counterexample and references, and checked the fixed-field construction."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Fields and Galois Theory (1) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMAF1 and carried its root-set and splitting-field proof as a second solution."
---

::: {.problem}
Let $K$ and $L$ be finite fields.
Show that $K$ is isomorphic to a subfield of $L$ if and only if
$\#K=p^r$ and $\#L=p^s$ for the same prime $p$, with $r\mid s$.
Here $r,s$ are positive integers.
:::

::: {.remark}
The inequality $r\leq s$ does not suffice. For example,
$\mathbb F_4$ cannot embed in $\mathbb F_8$, because the
tower law would require $2$ to divide $3$. Cardinalities
determine existence of an embedding, not literal inclusion
of arbitrary presentations of the fields. If both fields
are realized inside one algebraic closure of $\mathbb F_p$,
the criterion also characterizes literal subfield containment.
:::

::: {.solution}
Every finite field has prime characteristic and cardinality
a positive power of that prime [@DF04]. When an embedding
$K\hookrightarrow L$ is given, identify $K$ with its image.

<1>1. Forward direction ($K\hookrightarrow L\implies \operatorname{char} K = \operatorname{char} L = p$ and $r \mid s$):
<2>1. If $K$ is a subfield of $L$, then $L$ is a finite-dimensional vector space over $K$.
Let $d = [L : K] \ge 1$ denote the degree of the extension.
::: {.proof}
subfields endow the larger field with a vector space structure.
:::
<2>2. Since $K$ has characteristic $p$, $L$ must also have characteristic $p$.
The cardinality of $L$ is related to the cardinality of $K$ by:
\[
\# L = (\# K)^d = (p^r)^d = p^{rd}.
\]
::: {.proof}
a $d$-dimensional vector space over a field with $q$ elements contains $q^d$ elements.
:::
<2>3. Since $\# L = p^s$, we have $s = rd$, which implies $r \mid s$ (and therefore $r \le s$).
::: {.proof}
equating prime powers $p^s = p^{rd}$.
:::

<1>2. Reverse direction ($\#K = p^r, \, \#L = p^s$ with $r \mid s \implies K \hookrightarrow L$):
<2>1. If $r \mid s$, then $(p^r - 1) \mid (p^s - 1)$ because:
\[
x^k - 1 = (x - 1)(x^{k-1} + \dots + 1) \quad \text{applied to } x = p^r, \, s = kr.
\]
::: {.proof}
polynomial divisibility of $x^k - 1$ by $x - 1$.
:::
<2>2. The multiplicative group $L^\times$ is a cyclic group of order $p^s - 1$.
Since $(p^r - 1) \mid (p^s - 1)$, $L^\times$ contains a unique cyclic subgroup $H$ of order $p^r - 1$.
::: {.proof}
The multiplicative group of a finite field is cyclic,
and a cyclic group has exactly one subgroup for each
divisor of its order [@DF04].
:::
<2>3. The subset $K' = H \cup \{0\} \subseteq L$ consists precisely of all roots of the polynomial $f(x) = x^{p^r} - x \in \mathbb{F}_p[x]$ in $L$.
Since the map $\phi(x) = x^{p^r}$ is an automorphism of $L$ (the $r$-th power of the Frobenius automorphism), the fixed set:
\[
K' = \operatorname{Fix}(\phi) = \{\alpha \in L \mid \alpha^{p^r} = \alpha\}
\]
is a subfield of $L$.
::: {.proof}
The Frobenius map is an automorphism of a finite field,
and the fixed elements of any field automorphism form
a subfield [@DF04].
:::
<2>4. The subfield $K'$ has cardinality $\# K' = p^r = \# K$.
Since any two finite fields with $p^r$ elements are isomorphic, $K \cong K' \subseteq L$, so $K$ is isomorphic to a subfield of $L$.
::: {.proof}
Finite fields of the same cardinality are isomorphic [@DF04].
:::

<1>3. Conclusion:
$K$ embeds in $L$ if and only if $\#K=p^r$ and $\#L=p^s$
for the same prime $p$ with $r\mid s$.
::: {.proof}
This follows from <1>1 and <1>2. Inside a common algebraic
closure, any subfield with $p^r$ elements is exactly the
root set of $T^{p^r}-T$: all its elements are roots by
Lagrange's theorem and the polynomial has at most $p^r$
roots. Thus $K$ equals the constructed $K'$ in that
setting, proving the final assertion of the remark.
:::
:::

::: {.solution}
<1>1. An embedding forces the stated characteristic and divisibility.

::: {.proof}
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

::: {.proof}
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

::: {.proof}
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
