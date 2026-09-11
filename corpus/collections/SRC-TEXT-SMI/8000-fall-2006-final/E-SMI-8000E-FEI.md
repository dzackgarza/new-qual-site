---
schema: qual/card@1
id: E-SMI-8000E-FEI
kind: problem
title: Irreducibility and splitting fields of three polynomials
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared all three polynomials and all requested splitting-field questions with Smith 8000 Fall 2006 final part I."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Determined the Galois groups C3, S5, and C7 semidirect C6, the splitting-field degrees and real/solvable status, and classified every intermediate field normal over Q via the corresponding normal subgroups."
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared all three polynomials and all three requests with Smith 8000 Fall 2006 final part I."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Computed irreducibility, splitting-field degrees, real-root behavior, Galois groups, solvability, and the normal intermediate fields for all three polynomials; independently checked the two nontrivial discriminants exactly."
---

::: {.exercise}
Do all parts.
For each of the following polynomials over $\mathbb{Q}$:

(a) Prove the polynomial is irreducible over $\mathbb{Q}$.

(b) Say as much as you can about the splitting field $E$: the degree over $\mathbb{Q}$, whether or not it is a solvable extension, whether it is contained in $\mathbb{R}$, and compute the Galois group as well as you can.

(c) Say whatever you can about those intermediate fields between $E$ and $\mathbb{Q}$ which are normal over $\mathbb{Q}$.

(i) $X^3 - 3X + 1$

(ii) $X^5 - 20X + 4$

(iii) $X^7 - 2$
:::

::: solution
We treat the three polynomials separately.

## (i) $f(X)=X^3-3X+1$

<1>1. The cubic is irreducible over $\mathbb Q$.
::: proof
By the rational-root theorem, any rational root of the monic polynomial $f$
must be $\pm1$. But
$$
f(1)=-1,
\qquad
f(-1)=3.
$$
Thus $f$ has no rational root. A reducible cubic over a field has a linear
factor, so
$$
\boxed{f\text{ is irreducible over }\mathbb Q.}
$$
:::

<1>2. All three roots are real, and the discriminant is a square.
::: proof
The derivative is
$$
f'(x)=3(x^2-1).
$$
Thus $f$ is increasing on $(-\infty,-1)$, decreasing on $(-1,1)$, and
increasing on $(1,\infty)$. Moreover
$$
f(-1)=3>0,
\qquad
f(1)=-1<0,
$$
while
$$
f(x)\to-\infty\quad(x\to-\infty),
\qquad
f(x)\to\infty\quad(x\to\infty).
$$
Hence there is exactly one root in each of the three monotonicity intervals,
so all three roots are real.

For a depressed cubic $X^3+pX+q$, the discriminant is
$$
-4p^3-27q^2.
$$
Here $p=-3$ and $q=1$, so
$$
\Delta_f=-4(-3)^3-27=108-27=81=9^2.
$$
:::

<1>3. The splitting field has degree $3$ and Galois group $C_3$.
::: proof
Because $f$ is irreducible of degree three, its Galois group is a transitive
subgroup of $S_3$. The discriminant is a square in $\mathbb Q$, so the
Galois group lies in $A_3$. The only transitive subgroup of $A_3$ is $A_3$
itself. Therefore
$$
\boxed{\operatorname{Gal}(E/\mathbb Q)\cong A_3\cong C_3.}
$$
Consequently
$$
\boxed{[E:\mathbb Q]=3.}
$$
In particular the degree-three root field of any root already equals the
splitting field.

Since all roots are real,
$$
\boxed{E\subseteq\mathbb R.}
$$
The group $C_3$ is abelian, hence solvable, so this Galois extension is
solvable and the polynomial is solvable by radicals.
:::

<1>4. There are no nontrivial proper intermediate fields, hence no nontrivial proper normal ones.
::: proof
The Galois group $C_3$ has only the subgroups
$$
1
\quad\text{and}\quad
C_3.
$$
By the Galois correspondence the only intermediate fields are
$$
E
\quad\text{and}\quad
\mathbb Q.
$$
Both are of course normal over $\mathbb Q$.
:::

## (ii) $g(X)=X^5-20X+4$

<1>5. The quintic is irreducible over $\mathbb Q$.
::: proof
Translate the variable by one:
$$
\begin{aligned}
g(X+1)
&=(X+1)^5-20(X+1)+4\\
&=X^5+5X^4+10X^3+10X^2-15X-15.
\end{aligned}
$$
Every nonleading coefficient is divisible by $5$, while the constant term
$-15$ is not divisible by $25$. Eisenstein's criterion at $5$ therefore
shows that $g(X+1)$ is irreducible over $\mathbb Q$. Translation by one is an
automorphism of $\mathbb Q[X]$, so
$$
\boxed{g\text{ is irreducible over }\mathbb Q.}
$$
:::

<1>6. The polynomial has exactly three real roots.
::: proof
We have
$$
g'(x)=5x^4-20=5(x^4-4).
$$
Thus $g'$ is positive for $|x|>\sqrt2$ and negative for
$|x|<\sqrt2$. The two critical values are
$$
g(-\sqrt2)=4+16\sqrt2>0
$$
and
$$
g(\sqrt2)=4-16\sqrt2<0.
$$
Together with the limits at $\pm\infty$, the monotonicity intervals show that
$g$ has exactly one real root in each of
$$
(-\infty,-\sqrt2),
\qquad
(-\sqrt2,\sqrt2),
\qquad
(\sqrt2,\infty).
$$
Hence it has exactly three real roots and one nonreal conjugate pair.
:::

<1>7. The Galois group is $S_5$.
::: proof
Irreducibility makes the Galois group
$$
G\le S_5
$$
transitive on the five roots. Therefore
$$
5\mid |G|,
$$
so Cauchy's theorem gives an element of order $5$, necessarily a $5$-cycle.

Complex conjugation acts on the roots. By step <1>6 it fixes the three real
roots and swaps the two nonreal roots, so its action is a transposition.
Thus $G$ contains both a $5$-cycle and a transposition.

Conjugating the transposition by powers of the $5$-cycle gives
transpositions along the edges of a connected graph on the five roots. Edge
transpositions of a connected graph generate the full symmetric group.
Therefore
$$
\boxed{G=S_5.}
$$
Consequently
$$
\boxed{[E:\mathbb Q]=|S_5|=120.}
$$
:::

<1>8. This splitting field is neither real nor solvable.
::: proof
The splitting field contains the nonreal roots from step <1>6, so
$$
\boxed{E\not\subseteq\mathbb R.}
$$

The group $S_5$ is not solvable because it contains the nonabelian simple
normal subgroup $A_5$ and
$$
S_5/A_5\cong C_2.
$$
Hence
$$
\boxed{E/\mathbb Q\text{ is not a solvable Galois extension},}
$$
and the quintic is not solvable by radicals.
:::

<1>9. The only intermediate fields normal over $\mathbb Q$ are $\mathbb Q$, the quadratic discriminant field, and $E$.
::: proof
The normal subgroups of $S_5$ are
$$
1,
\qquad
A_5,
\qquad
S_5.
$$
Indeed, if $N\trianglelefteq S_5$, then
$N\cap A_5\trianglelefteq A_5$. Simplicity of $A_5$ gives
$N\cap A_5=1$ or $A_5$. In the second case $N=A_5$ or $S_5$; in the first,
$N$ injects into $S_5/A_5\cong C_2$, and a nontrivial normal subgroup of
order two would be central, impossible because $Z(S_5)=1$.

Thus the normal intermediate fields are
$$
E,
\qquad
E^{A_5},
\qquad
\mathbb Q.
$$
The middle field is generated by the square root of the discriminant. A
direct discriminant computation for $X^5+aX+b$ gives
$$
\Delta=5^5b^4+4^4a^5,
$$
so here
$$
\Delta_g
=5^5\cdot4^4+4^4(-20)^5
=-818400000
=-2^8\cdot3\cdot5^5\cdot11\cdot31.
$$
Its square class is $-5115$, hence
$$
\boxed{E^{A_5}=\mathbb Q(\sqrt{-5115}).}
$$
:::

## (iii) $h(X)=X^7-2$

<1>10. The polynomial is irreducible over $\mathbb Q$.
::: proof
All nonleading coefficients of
$$
X^7-2
$$
are divisible by $2$, and its constant term is not divisible by $4$.
Eisenstein's criterion at $2$ gives
$$
\boxed{X^7-2\text{ irreducible over }\mathbb Q.}
$$
:::

<1>11. Describe the splitting field and compute its degree.
::: proof
Let
$$
\alpha=2^{1/7}>0
$$
and let $\zeta=\zeta_7$ be a primitive seventh root of unity. The seven roots
are
$$
\alpha,\zeta\alpha,\ldots,\zeta^6\alpha,
$$
so the splitting field is
$$
E=\mathbb Q(\alpha,\zeta).
$$

Eisenstein gives
$$
[\mathbb Q(\alpha):\mathbb Q]=7,
$$
while cyclotomic theory gives
$$
[\mathbb Q(\zeta):\mathbb Q]=\varphi(7)=6.
$$
The degree of their intersection divides both $7$ and $6$, hence
$$
\mathbb Q(\alpha)\cap\mathbb Q(\zeta)=\mathbb Q.
$$
Therefore
$$
\boxed{[E:\mathbb Q]=7\cdot6=42.}
$$
:::

<1>12. The Galois group is the faithful semidirect product $C_7\rtimes C_6$.
::: proof
Define
$$
\sigma(\alpha)=\zeta\alpha,
\qquad
\sigma(\zeta)=\zeta.
$$
Then $\sigma$ has order $7$.

Since the two subfields in step <1>11 have trivial intersection, the
automorphism of $\mathbb Q(\zeta)$ defined by
$$
\zeta\longmapsto\zeta^3
$$
extends while fixing $\alpha$. Thus there is an automorphism $\tau$ with
$$
\tau(\alpha)=\alpha,
\qquad
\tau(\zeta)=\zeta^3.
$$
Because $3$ has order $6$ modulo $7$, the automorphism $\tau$ has order $6$.
Moreover
$$
\tau\sigma\tau^{-1}=\sigma^3.
$$

The $42$ elements
$$
\sigma^i\tau^j,
\qquad
0\le i<7,
\quad
0\le j<6,
$$
are distinct. Since the splitting field has degree $42$, they exhaust its
Galois group. Hence
$$
\boxed{
\operatorname{Gal}(E/\mathbb Q)
\cong C_7\rtimes C_6,}
$$
where a generator of $C_6$ acts on $C_7$ by multiplication by $3$ modulo
$7$.
:::

<1>13. The extension is solvable but not contained in $\mathbb R$.
::: proof
The normal subgroup
$$
\langle\sigma\rangle\cong C_7
$$
has quotient $C_6$. Both are abelian, so the Galois group is solvable; in
fact its commutator subgroup is contained in $C_7$. Hence
$$
\boxed{E/\mathbb Q\text{ is solvable},}
$$
and $X^7-2$ is solvable by radicals.

On the other hand, $E$ contains the nonreal primitive seventh root of unity
$\zeta$, so
$$
\boxed{E\not\subseteq\mathbb R.}
$$
:::

<1>14. Classify all intermediate fields normal over $\mathbb Q$.
::: proof
Put
$$
N=\langle\sigma\rangle\cong C_7.
$$
Then
$$
G/N\cong C_6.
$$
We first classify the normal subgroups of $G$.

If $K\trianglelefteq G$, then
$$
K\cap N\trianglelefteq N.
$$
Since $|N|=7$ is prime,
$$
K\cap N=1
\quad\text{or}\quad
N.
$$
If $K\cap N=1$, then for $k\in K$ and $n\in N$ the commutator
$[k,n]$ lies in both $K$ and $N$, hence is trivial. Thus $K$ centralizes
$N$. The action of $C_6$ on $N$ is faithful, so
$$
C_G(N)=N.
$$
Therefore $K\le N$, and the trivial intersection forces $K=1$.

If $N\le K$, then $K/N$ is a subgroup of the cyclic group $G/N\cong C_6$.
Conversely, the inverse image of every subgroup of the abelian quotient
$C_6$ is normal. Hence the normal subgroups are precisely
$$
1,
\quad
N,
\quad
N\rtimes C_2,
\quad
N\rtimes C_3,
\quad
G.
$$

Their fixed fields are therefore exactly the intermediate fields normal over
$\mathbb Q$. They may be identified inside the cyclotomic subfield
$$
E^N=\mathbb Q(\zeta_7).
$$
Thus the complete list is
$$
\boxed{
\begin{aligned}
&E,\\
&\mathbb Q(\zeta_7),\\
&\mathbb Q(\zeta_7+\zeta_7^{-1}),\\
&\mathbb Q(\sqrt{-7}),\\
&\mathbb Q.
\end{aligned}}
$$
The degrees over $\mathbb Q$ are respectively
$$
42,\ 6,\ 3,\ 2,\ 1.
$$
The cubic field is the maximal real subfield of $\mathbb Q(\zeta_7)$, fixed
by complex conjugation, and $\mathbb Q(\sqrt{-7})$ is its unique quadratic
subfield.
:::
:::

::: solution
Write
$$
f_3(X)=X^3-3X+1,
\qquad
f_5(X)=X^5-20X+4,
\qquad
f_7(X)=X^7-2.
$$

<1>1. Analyze $f_3(X)=X^3-3X+1$.
::: proof
The rational-root theorem leaves only $\pm1$ as possible rational roots, and
$$
f_3(1)=-1,
\qquad
f_3(-1)=3.
$$
Thus the cubic has no rational root and is irreducible over $\mathbb Q$.

For a depressed cubic $X^3+pX+q$, the discriminant is
$$
-4p^3-27q^2.
$$
Here
$$
\Delta_3=-4(-3)^3-27=81=9^2.
$$
An irreducible cubic has transitive Galois group in $S_3$; its discriminant
is a square exactly when the group lies in $A_3$. Hence
$$
\operatorname{Gal}(E_3/\mathbb Q)\cong A_3\cong C_3,
$$
and therefore
$$
[E_3:\mathbb Q]=3.
$$

All three roots are real: indeed
$$
f_3(-2)<0<f_3(-1),
$$
$$
f_3(0)>0>f_3(1),
$$
and
$$
f_3(1)<0<f_3(2).
$$
Thus the three distinct roots lie in the disjoint intervals
$(-2,-1)$, $(0,1)$, and $(1,2)$, so
$$
E_3\subseteq\mathbb R.
$$

The Galois group is cyclic, hence solvable. Since its order is prime, its only
subgroups are $1$ and the whole group. Therefore the only intermediate fields
normal over $\mathbb Q$ are
$$
\boxed{\mathbb Q\quad\text{and}\quad E_3.}
$$
:::

<1>2. Prove $f_5(X)=X^5-20X+4$ is irreducible.
::: proof
Translate by $1$:
$$
\begin{aligned}
f_5(X+1)
&=(X+1)^5-20(X+1)+4\\
&=X^5+5X^4+10X^3+10X^2-15X-15.
\end{aligned}
$$
Every nonleading coefficient is divisible by $5$, while the constant term
$-15$ is not divisible by $25$. Eisenstein's criterion at $5$ therefore shows
that $f_5(X+1)$ is irreducible over $\mathbb Q$. Translation preserves
irreducibility, so
$$
\boxed{f_5\text{ is irreducible over }\mathbb Q.}
$$
:::

<1>3. Determine the real roots and Galois group of $f_5$.
::: proof
The derivative is
$$
f_5'(x)=5x^4-20=5(x^4-4).
$$
Its real critical points are $\pm\sqrt2$. Moreover
$$
f_5(-\sqrt2)=4+16\sqrt2>0,
$$
whereas
$$
f_5(\sqrt2)=4-16\sqrt2<0.
$$
Since $f_5(x)\to-\infty$ as $x\to-\infty$ and
$f_5(x)\to+\infty$ as $x\to+\infty$, the monotonicity intervals determined
by these two critical points show that $f_5$ has exactly three real roots.
The remaining two roots form one nonreal conjugate pair.

Let $G_5$ be the Galois group of the splitting field, acting on the five
roots. Irreducibility makes this action transitive, so $5$ divides $|G_5|$;
by Cauchy's theorem $G_5$ contains a $5$-cycle. Complex conjugation fixes the
three real roots and interchanges the nonreal pair, so it is a transposition
in $G_5$.

A $5$-cycle together with any transposition generates $S_5$: conjugating the
transposition by powers of the $5$-cycle gives the edge transpositions of a
connected graph on the five letters, and transpositions along the edges of a
connected graph generate the full symmetric group. Thus
$$
\boxed{G_5\cong S_5.}
$$
Consequently
$$
\boxed{[E_5:\mathbb Q]=120.}
$$
Since $S_5$ is not solvable, $E_5/\mathbb Q$ is not a solvable Galois
extension. Since $E_5$ contains the nonreal roots,
$$
E_5\not\subseteq\mathbb R.
$$
:::

<1>4. Determine the normal intermediate fields for $f_5$.
::: proof
The discriminant is
$$
\Delta_5=-818400000
=-400^2\cdot5115.
$$
Hence
$$
\mathbb Q(\sqrt{\Delta_5})
=\mathbb Q(\sqrt{-5115}).
$$

The normal subgroups of $S_5$ are
$$
1,
\qquad
A_5,
\qquad
S_5.
$$
Indeed, if $N\trianglelefteq S_5$, then $N\cap A_5\trianglelefteq A_5$.
Since $A_5$ is simple, this intersection is either $1$ or $A_5$. In the
second case, either $N=A_5$ or $N=S_5$. In the first case, the quotient map
$S_5\to S_5/A_5\cong C_2$ is injective on $N$, so $|N|\le2$. If $N$ were a
nontrivial subgroup of order two, its nonidentity element would be an odd
involution, hence a transposition. Normality would then force $N$ to contain
all conjugate transpositions, impossible for a group of order two. Thus
$N=1$.

By the Galois correspondence, the intermediate fields normal over
$\mathbb Q$ are therefore exactly the fixed fields of these three subgroups:
$$
\boxed{
E_5,
\qquad
\mathbb Q(\sqrt{\Delta_5})=\mathbb Q(\sqrt{-5115}),
\qquad
\mathbb Q.}
$$
Here the quadratic field is the fixed field of $A_5$.
More explicitly, if $r_1,\ldots,r_5$ are the roots and
$$
\delta=\prod_{i<j}(r_i-r_j),
$$
then $\delta^2=\Delta_5$, and a permutation of the roots sends $\delta$ to
its sign times $\delta$. Hence the stabilizer of $\delta$ in $S_5$ is exactly
$A_5$, so
$$
E_5^{A_5}=\mathbb Q(\delta)=\mathbb Q(\sqrt{\Delta_5}).
$$
:::

<1>5. Prove $f_7(X)=X^7-2$ is irreducible and describe its splitting field.
::: proof
Eisenstein's criterion at $2$ applies directly to
$$
X^7-2,
$$
so $f_7$ is irreducible over $\mathbb Q$.

Let
$$
\alpha=2^{1/7}>0
$$
and let $\zeta=\zeta_7$ be a primitive seventh root of unity. The seven roots
are
$$
\alpha,\zeta\alpha,\ldots,\zeta^6\alpha,
$$
so the splitting field is
$$
E_7=\mathbb Q(\alpha,\zeta).
$$
Now
$$
[\mathbb Q(\alpha):\mathbb Q]=7,
\qquad
[\mathbb Q(\zeta):\mathbb Q]=\varphi(7)=6.
$$
The degree of their intersection divides both $7$ and $6$, hence
$$
\mathbb Q(\alpha)\cap\mathbb Q(\zeta)=\mathbb Q.
$$
Therefore
$$
\boxed{[E_7:\mathbb Q]=7\cdot6=42.}
$$
Because $\zeta\notin\mathbb R$,
$$
E_7\not\subseteq\mathbb R.
$$
:::

<1>6. Compute the Galois group of $f_7$ and its solvability.
::: proof
Define automorphisms
$$
\sigma(\alpha)=\zeta\alpha,
\qquad
\sigma(\zeta)=\zeta,
$$
and, taking $3$ as a generator of $(\mathbb Z/7\mathbb Z)^\times$,
$$
\tau(\alpha)=\alpha,
\qquad
\tau(\zeta)=\zeta^3.
$$
The second map exists because the degree computation in step <1>5 gives
$\mathbb Q(\alpha)\cap\mathbb Q(\zeta)=\mathbb Q$, so the cyclotomic
automorphisms extend to the compositum while fixing $\alpha$.
Then
$$
\sigma^7=1,
\qquad
\tau^6=1,
$$
and
$$
\tau\sigma\tau^{-1}=\sigma^3.
$$
The subgroup generated by $\sigma$ and $\tau$ therefore has the form
$$
C_7\rtimes C_6,
$$
where $C_6\cong(\mathbb Z/7\mathbb Z)^\times$ acts faithfully on $C_7$.
It has $42$ elements, equal to the degree of the splitting field, so
$$
\boxed{
\operatorname{Gal}(E_7/\mathbb Q)
\cong C_7\rtimes C_6
\cong \operatorname{AGL}_1(\mathbb F_7).}
$$

This group is solvable: it has the normal cyclic subgroup $C_7$ with cyclic
quotient $C_6$. Thus $E_7/\mathbb Q$ is a solvable Galois extension.
:::

<1>7. Classify the normal intermediate fields for $f_7$.
::: proof
Let
$$
N=\langle\sigma\rangle\cong C_7.
$$
Then $N\trianglelefteq G_7$ and
$$
G_7/N\cong C_6.
$$
The preimages of the four subgroups of $C_6$ are normal in $G_7$, giving
normal subgroups of orders
$$
7,14,21,42.
$$
Together with the trivial subgroup, these are all the normal subgroups.
Indeed, if $K\trianglelefteq G_7$ and $K\cap N=1$, then
$$
[K,N]\subseteq K\cap N=1,
$$
so $K$ centralizes $N$. The faithful semidirect action implies
$$
C_{G_7}(N)=N,
$$
and hence $K=1$.

Thus the normal subgroups are exactly
$$
1,
\quad
N,
\quad
N\rtimes C_2,
\quad
N\rtimes C_3,
\quad
G_7.
$$
Their fixed fields all lie in $\mathbb Q(\zeta)$ because $N$ fixes
$\zeta$. The corresponding normal intermediate fields are
$$
\boxed{
E_7,
\quad
\mathbb Q(\zeta_7),
\quad
\mathbb Q(\zeta_7+\zeta_7^{-1}),
\quad
\mathbb Q(\sqrt{-7}),
\quad
\mathbb Q.}
$$
Indeed the subgroup of order $2$ in
$\operatorname{Gal}(\mathbb Q(\zeta_7)/\mathbb Q)\cong C_6$ is complex
conjugation, so its fixed field is the real cubic field
$\mathbb Q(\zeta_7+\zeta_7^{-1})$; the subgroup of order $3$ fixes the unique
quadratic subfield $\mathbb Q(\sqrt{-7})$.
:::
:::
