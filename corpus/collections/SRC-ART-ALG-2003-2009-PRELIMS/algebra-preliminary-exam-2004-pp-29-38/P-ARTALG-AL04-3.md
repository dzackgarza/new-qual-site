---
schema: qual/card@1
id: P-ARTALG-AL04-3
kind: problem
title: 'The fifty groups of order $72$'
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked the retained PDF, page 30 (printed page 2), Groups 3: the order is the integer 72, not 7 squared, and there is no abelian hypothesis."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the three exhaustive Sylow cases, all semidirect actions, the residual fiber-product reduction, and the exact matrix-action orbit enumeration without a small-group catalogue."
---

::: problem
List all isomorphism classes of groups of size $72$.
:::

::: solution
There are exactly $50$ classes. The list consists of the $42$ semidirect
products in step <1>1, the four groups in step <1>3, and the four groups
in step <1>4. In particular, restricting to abelian groups would not
answer the question.

Write $C_m=\mathbb Z/m\mathbb Z$, and use $D_{2m}$ for the dihedral
group of order $2m$. For an action $\phi:H\to\operatorname{Aut}(N)$,
$N\rtimes_\phi H$ has multiplication
$(n,h)(n',h')=(n\phi(h)(n'),hh')$, with additive notation when $N$
is a vector space. Every action used below is specified on generators.

<1>1. The groups with normal Sylow $3$-subgroup are precisely the
following $42$ groups $N\rtimes H$.

For $N=C_9$, the symbol $+$ denotes the identity automorphism and $-$
denotes inversion. For $N=C_3^2$, identify $N$ with $\mathbb F_3^2$
of column vectors and use these matrices over $\mathbb F_3$:
$$
I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
Z=-I,\quad D=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
A=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
B=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
C=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
$$
Each tuple in a table entry gives the images of the ordered generators
of $H$ and specifies one group, not an unspecified semidirect product.

| $H$ and generators | Actions on $C_9$ | Actions on $C_3^2$ |
| --- | --- | --- |
| $C_8=\langle r\rangle$ | $+$; $-$ | $I$; $Z$; $D$; $A$; $C$ |
| $C_4\times C_2=\langle r\rangle\times\langle s\rangle$ | $(+,+)$; $(-,+)$; $(+,-)$ | $(I,I)$; $(Z,I)$; $(I,Z)$; $(D,I)$; $(I,D)$; $(D,Z)$; $(Z,D)$; $(A,I)$ |
| $C_2^3=\langle r,s,w\rangle$ | $(+,+,+)$; $(-,+,+)$ | $(I,I,I)$; $(Z,I,I)$; $(D,I,I)$; $(Z,D,I)$ |
| $D_8=\langle r,s\mid r^4=s^2=1,\ srs^{-1}=r^{-1}\rangle$ | $(+,+)$; $(+,-)$; $(-,+)$ | $(I,I)$; $(I,Z)$; $(I,D)$; $(Z,I)$; $(Z,D)$; $(D,I)$; $(D,Z)$; $(A,D)$ |
| $Q_8=\langle r,s\mid r^4=1,\ s^2=r^2,\ srs^{-1}=r^{-1}\rangle$ | $(+,+)$; $(-,+)$ | $(I,I)$; $(Z,I)$; $(D,I)$; $(Z,D)$; $(A,B)$ |

There are $2+3+2+3+2=12$ groups in the second column and
$5+8+4+8+5=30$ in the third.

::: proof
A group of order $9$ is abelian: its center is nontrivial by the
class equation; if its center had order $3$, its quotient by the
center would be cyclic, which forces the whole group to be abelian.
Indeed, writing every element as $g^i z$ with $z$ central shows that
any two elements commute. Thus the normal Sylow subgroup $N$ is
$C_9$ or $C_3^2$. A Sylow $2$-subgroup $H$ has order $8$, with
$N\cap H=1$ and $NH=G$, so $G=N\rtimes H$.
The five groups of order $8$ are exactly those in the table [@DF04].

The subgroup $N$ is characteristic because it is the unique Sylow
$3$-subgroup. Conjugation on the abelian group $N$ defines an action
of $G/N$ independent of the chosen lifts. Consequently two actions
give isomorphic groups exactly when one can be changed to the other
by an automorphism of $H$ and conjugation by an automorphism of $N$.
Necessity follows by restricting an isomorphism to $N$ and passing
to the quotient; sufficiency follows by applying these two
automorphisms to the two coordinates of the semidirect product.
Different kernel types or quotient types cannot be isomorphic.

For $N=C_9$, its automorphism group is $(\mathbb Z/9\mathbb Z)^\times$,
of order $6$, whose only elements of $2$-power order are $+$ and $-$.
Thus every action takes values in this two-element subgroup.
For $C_8$ there are two homomorphisms. For $C_4\times C_2$, its
automorphisms have the form
$$
r\mapsto r^\varepsilon s^e,\quad s\mapsto r^{2f}s,
\qquad \varepsilon\in\{1,3\},\quad e,f\in\{0,1\}.
$$
On the two signs $(R,S)$ this replaces $R$ by $RS^e$ and leaves
$S$ fixed, giving exactly its three listed orbits. For $C_2^3$,
the automorphism group is transitive on nonzero linear functionals
to $C_2$, giving two orbits. For $D_8$, the automorphisms are
$r\mapsto r^{\pm1}$, $s\mapsto r^k s$; thus $R$ is fixed and
$S$ can be replaced by $R^kS$, giving the three displayed pairs.
For $Q_8$, every sign homomorphism factors through $Q_8/\langle
r^2\rangle\cong C_2^2$. Permuting its three cyclic subgroups of
order $4$ induces all automorphisms of this quotient, giving two
orbits. This proves completeness and distinctness in the $C_9$ column.

For $C_3^2$, the automorphism group is $\operatorname{GL}_2(\mathbb F_3)$.
Step <1>2 gives an exhaustive, executable verification of precisely
the action orbits in the third column. Together with the preceding
isomorphism criterion, this proves all assertions about the $42$ groups.
:::

<1>2. The matrix-action column is exhaustive and has no repeated orbit.

::: proof
Represent a matrix by its four row-major entries. There are exactly
the invertible matrices in the finite set $\{0,1,2\}^4$ to check.
A tuple determines a homomorphism from a presented group exactly
when it satisfies all the defining relations. The function `valid`
below tests those relations; `candidates` therefore contains every
homomorphism, not just selected examples.

The function `changes` enumerates every change of generators induced
by an automorphism of the source. For the cyclic group these are the
odd powers. The formulas for $C_4\times C_2$ and $D_8$ were given
in step <1>1. In $C_4\times C_2$, the image of $r$ can be any
of its four elements of order $4$, and the image of $s$ must be
one of the two involutions outside that cyclic subgroup, giving
exactly the stated formula. In $D_8$, the unique cyclic subgroup
of order $4$ must be preserved, and the image of $s$ can be any
of the four reflections. For $C_2^3$ the changes are all ordered binary bases. For
$Q_8$, an automorphism sends $r,s$ to elements of order $4$ on two
different cyclic axes. Such elements square to $-1$, anticommute,
and generate $Q_8$, so all $6\cdot4=24$ choices work.
The three axes in normal form $r^a s^b$ are exactly those listed
in the code. Thus `orbit` enumerates the entire
$\operatorname{Aut}(H)\times\operatorname{GL}_2(\mathbb F_3)$-orbit.

The calculation checks that the listed orbits are disjoint and that
their union equals `candidates`. All arithmetic is exact modulo $3$;
no finite-group catalogue, probabilistic test, or precomputed
classification is used.

```python
from itertools import product, combinations

I = (1, 0, 0, 1)
Z = (2, 0, 0, 2)
D = (1, 0, 0, 2)
A = (0, 2, 1, 0)
B = (1, 1, 1, 2)
C = (0, 1, 1, 1)

def mul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return ((a*e+b*g) % 3, (a*f+b*h) % 3,
            (c*e+d*g) % 3, (c*f+d*h) % 3)

def power(x, n):
    result = I
    for _ in range(n):
        result = mul(result, x)
    return result

def inverse(x):
    a, b, c, d = x
    u = pow((a*d-b*c) % 3, -1, 3)
    return ((u*d) % 3, (-u*b) % 3, (-u*c) % 3, (u*a) % 3)

GL = [x for x in product(range(3), repeat=4)
      if (x[0]*x[3]-x[1]*x[2]) % 3 != 0]
table = {
    "C8": [(I,), (Z,), (D,), (A,), (C,)],
    "C4xC2": [(I,I), (Z,I), (I,Z), (D,I),
              (I,D), (D,Z), (Z,D), (A,I)],
    "C2^3": [(I,I,I), (Z,I,I), (D,I,I), (Z,D,I)],
    "D8": [(I,I), (I,Z), (I,D), (Z,I),
           (Z,D), (D,I), (D,Z), (A,D)],
    "Q8": [(I,I), (Z,I), (D,I), (Z,D), (A,B)],
}

vectors = [v for v in product(range(2), repeat=3) if any(v)]

def xor(x, y):
    return tuple((a+b) % 2 for a, b in zip(x, y))

bases = [(u,v,w) for u,v,w in product(vectors, repeat=3)
         if len({(0,0,0), u, v, w, xor(u,v), xor(u,w),
                 xor(v,w), xor(xor(u,v),w)}) == 8]

def valid(name, t):
    if name == "C8":
        return power(t[0], 8) == I
    if name == "C2^3":
        return (all(power(x, 2) == I for x in t)
                and all(mul(x,y) == mul(y,x)
                        for x,y in combinations(t, 2)))
    r, s = t
    if name == "C4xC2":
        return (power(r,4) == I and power(s,2) == I
                and mul(r,s) == mul(s,r))
    if name == "D8":
        return (power(r,4) == I and power(s,2) == I
                and mul(s,r) == mul(power(r,3),s))
    if name == "Q8":
        return (power(r,4) == I and power(s,2) == power(r,2)
                and mul(s,r) == mul(power(r,3),s))
    raise ValueError(name)

def changes(name, t):
    if name == "C8":
        return [(power(t[0], k),) for k in (1,3,5,7)]
    if name == "C2^3":
        def value(v):
            ans = I
            for x, e in zip(t, v):
                ans = mul(ans, power(x,e))
            return ans
        return [tuple(value(v) for v in basis) for basis in bases]
    r, s = t
    if name == "C4xC2":
        return [(mul(power(r,e),power(s,f)), mul(power(r,2*g),s))
                for e,f,g in product((1,3),(0,1),(0,1))]
    if name == "D8":
        return [(power(r,e), mul(power(r,k),s))
                for e,k in product((1,3),range(4))]
    if name == "Q8":
        axes = [[(1,0),(3,0)], [(0,1),(2,1)], [(1,1),(3,1)]]
        def value(v):
            return mul(power(r,v[0]), power(s,v[1]))
        return [(value(u),value(v))
                for i,j in product(range(3), repeat=2) if i != j
                for u in axes[i] for v in axes[j]]
    raise ValueError(name)

def orbit(name, t):
    result = set()
    for changed in changes(name, t):
        for m in GL:
            mi = inverse(m)
            result.add(tuple(mul(mul(m,x),mi) for x in changed))
    return result

for name, reps in table.items():
    candidates = {t for t in product(GL, repeat=len(reps[0]))
                  if valid(name,t)}
    seen = set()
    for rep in reps:
        if not valid(name,rep):
            raise ValueError(("bad representative", name, rep))
        current = orbit(name,rep)
        if current & seen:
            raise ValueError(("repeated orbit", name, rep))
        seen.update(current)
    if seen != candidates:
        raise ValueError(("incomplete", name, len(seen), len(candidates)))
    print(name, len(candidates), len(reps))
```

Its output gives the number of homomorphisms followed by the number
of distinct action orbits:

```text
C8 32 5
C4xC2 88 8
C2^3 344 4
D8 100 8
Q8 100 5
```
:::

<1>3. Exactly four further groups have a normal Sylow $2$-subgroup.

Let $V=C_2^3=\mathbb F_2\oplus\mathbb F_2^2$, and let $\tau_V$
fix the first coordinate and act on the second summand by
$\left(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right)$.
Let $Q_8=\{\pm1,\pm i,\pm j,\pm k\}$ with $ij=k$, and let
$\tau_Q$ cyclically permute $i,j,k$. Both automorphisms have order $3$.
The four groups are
$$
V\rtimes C_9,\qquad V\rtimes(C_3\times C_3),\qquad
Q_8\rtimes C_9,\qquad Q_8\rtimes(C_3\times C_3),
$$
where a generator of $C_9$ acts by the indicated $\tau$, or the
first $C_3$ factor acts by $\tau$ and the second acts trivially.

::: proof
Let $T$ be a normal Sylow $2$-subgroup and $P$ a Sylow $3$-subgroup.
Then $G=T\rtimes P$, with $P=C_9$ or $C_3^2$. For the five possible
types of $T$, the respective automorphism-group orders are
$$
\begin{array}{c|ccccc}
T&C_8&C_4\times C_2&C_2^3&D_8&Q_8\\\hline
|\operatorname{Aut}(T)|&4&8&168&8&24.
\end{array}
$$
The cyclic case counts odd generator powers; the generator formulas
in step <1>1 give the two orders $8$; the order $168=(8-1)(8-2)(8-4)$
counts ordered bases; and the quaternion count is $6\cdot4=24$ as
in step <1>2.

For $C_8,C_4\times C_2,D_8$, a homomorphism from the order-$9$
group to this automorphism group is trivial. For $V,Q_8$, its image
has order $1$ or $3$. A trivial action gives a direct product
already in step <1>1. Every subgroup of order $3$ in either
automorphism group is Sylow, so all such subgroups are conjugate.
The displayed $\tau_V,\tau_Q$ show that nontrivial actions exist.
Changing a generator of $C_9$, or changing a basis of $C_3^2$,
identifies all surjections onto one such $C_3$. Thus precisely the
four displayed nontrivial actions remain.

They are distinct: their Sylow $2$-subgroups distinguish $V$ from
$Q_8$, and their Sylow $3$-subgroups distinguish $C_9$ from $C_3^2$.
None belongs to step <1>1. If both Sylow subgroups were normal,
their commutators would lie in their trivial intersection, forcing
the action to be trivial.
:::

<1>4. The remaining four groups are
$$
S_3\times A_4,\qquad C_3\times S_4,\qquad
C_3\rtimes_{\mathrm{sgn}}S_4,\qquad
D_{18}\times_{S_3}S_4.
$$
For the third group, an even permutation acts trivially on $C_3$
and an odd permutation acts by inversion. Define the fourth group
as follows. Put
$$
D_{18}=\langle u,v\mid u^9=v^2=1,\ vuv^{-1}=u^{-1}\rangle.
$$
Let $q:D_{18}\to S_3$ send $u$ to $(123)$ and $v$ to $(12)$.
Let $\pi:S_4\to S_3$ be its action on the three partitions of four
letters into two unordered pairs. Then
$$
D_{18}\times_{S_3}S_4
=\{(d,s)\in D_{18}\times S_4:q(d)=\pi(s)\},
$$
with coordinatewise multiplication. Both maps are onto, so this
group has order $18\cdot24/6=72$.

::: proof
<2>1. Suppose neither Sylow subgroup of $G$ is normal. There are
four Sylow $3$-subgroups, since their number divides $8$ and is
$1$ modulo $3$. Let $K$ be the kernel of conjugation on these
four subgroups. The image is transitive in $S_4$, so its order
is a multiple of $4$ dividing $24$ and $72$: it is $4,8,12$, or $24$.

In the first two cases $|K|=18$ or $9$, and the image is a
$2$-group. Every Sylow $3$-subgroup of $G$ would then lie in $K$.
But either of these orders gives a unique Sylow $3$-subgroup in
$K$, a contradiction. Therefore $|K|=6$ or $3$. In the first
case the image is the unique index-two subgroup $A_4$ of $S_4$;
in the second the image is $S_4$.

We use that $[S_4,S_4]=A_4$ and $[A_4,A_4]=V_4$, where $V_4$
is the subgroup of double transpositions. The relevant quotients
are abelian; commutators of transpositions include $3$-cycles and
their conjugates generate $A_4$, while
$[(123),(124)]=(12)(34)$, using $[x,y]=xyx^{-1}y^{-1}$.
Its conjugates in $A_4$ generate $V_4$. This proves
both equalities. In particular the only nontrivial map $S_4\to C_2$
is sign, and there is no nontrivial map $A_4\to C_2$.

<2>2. Consider $|K|=6$. A group of order $6$ is $C_6$ or $S_3$:
its normal Sylow $3$-subgroup has an order-two complement, which
acts either trivially or by inversion.

If $K=C_6$, let $N$ be its characteristic subgroup of order $3$.
Conjugation on $N$ factors through $G/K=A_4$, since $K$ is abelian.
The preceding observation makes this action trivial, so $N$ is
central in $G$. Let $U$ be the inverse image of $V_4\lhd A_4$;
then $U\lhd G$ has order $24$. A Sylow $2$-subgroup $T$ of $U$
commutes with $N$ and gives $U=N\times T$. In this direct product
the elements of $2$-power order form exactly $T$, so $T$ is
characteristic in $U$ and normal in $G$. This contradicts the
assumption on the Sylow $2$-subgroups.

Thus $K=S_3$. Every automorphism of $S_3$ is inner: it permutes
the three transpositions, giving an injection into $S_3$, and
conjugation already realizes all six permutations because the
center is trivial. For every $g\in G$, choose $k\in K$ with the
same conjugation action on $K$. Then $k^{-1}g\in C_G(K)$, so
$G=K C_G(K)$. The intersection is $Z(K)=1$, and the two factors
commute. Consequently
$G\cong K\times C_G(K)\cong S_3\times A_4$.

<2>3. Consider $K=N=C_3$, with $G/N\cong S_4$. Conjugation on
$N$ factors through $S_4$ and is trivial or sign. In particular
the inverse image $U$ of $V_4$ centralizes $N$. It has order $12$;
choosing a Sylow $2$-subgroup $V$ gives $U=N\times V$, just as
in <2>2. Thus $V\cong V_4$ is characteristic in $U$, hence
normal in $G$.

Set $H=G/V$. Then $|H|=18$ and the induced map $q_H:H\to S_3$
has kernel the image of $N$, of order $3$. The map
$$
G\longrightarrow H\times S_4,\qquad
g\longmapsto(gV,gN)
$$
is injective because $V\cap N=1$, and its image lies in the
fiber product of $q_H$ and $\pi$. That fiber product has order
$18\cdot24/6=72$, so the map is an isomorphism onto it.

<2>4. There are exactly three possibilities for the pair $(H,\ker q_H)$.
Let $P$ be its unique Sylow $3$-subgroup of order $9$ and let $t$
be an involution, so $H=P\rtimes\langle t\rangle$. The quotient
$P/\ker q_H=C_3$ is inverted by $t$, since $H/\ker q_H=S_3$.

If $P=C_9$, the only automorphisms of order dividing $2$ are the
identity and inversion, and the quotient condition forces
inversion. Thus $H=D_{18}$ with its unique subgroup of order $3$
as kernel.

If $P=C_3^2$, the involution on this vector space is diagonalizable:
each vector is the sum of $(x+t x)/2$ and $(x-t x)/2$, in the
$+1$ and $-1$ eigenspaces respectively. The quotient has eigenvalue
$-1$. If the kernel has eigenvalue $+1$, the two eigenspaces give
$H=C_3\times S_3$ with its central $C_3$ as kernel. If the kernel
has eigenvalue $-1$, the involution is $-I$, so
$H=C_3^2\rtimes_{-I}C_2$; all choices of a kernel line are
equivalent under $\operatorname{GL}_2(\mathbb F_3)$.

Any two quotient identifications differ by an automorphism of
$S_3$, which is inner. Conjugation by a lift in $S_4$ absorbs
that change in the fiber product. Therefore no extra classes
arise from the choice of the quotient map.
The first case gives $D_{18}\times_{S_3}S_4$. The second gives
$C_3\times S_4$. In the last case split $C_3^2$ as the kernel
line plus another line. Both are inverted by $t$, so the pullback
is $C_3\rtimes_{\mathrm{sgn}}S_4$. This proves exhaustiveness.

<2>5. All four groups exist and are distinct, and none belongs to
steps <1>1 or <1>3. For each of the three groups projecting onto
$S_4$ with kernel $C_3$, inverse images of its four Sylow
$3$-subgroups are precisely the four Sylow $3$-subgroups of the
order-$72$ group. A normal Sylow $2$-subgroup would project to a
normal Sylow $2$-subgroup of $S_4$, which does not exist: the quotient
$S_4\to S_3$ would map such a subgroup onto a normal order-two
subgroup of $S_3$, whereas its three transposition subgroups are
distinct and conjugate. For $S_3\times A_4$, the Sylow counts are
likewise $n_3=4$ and $n_2=3$: $S_3$ has one Sylow $3$-subgroup
and three Sylow $2$-subgroups, while $A_4$ has four Sylow
$3$-subgroups and its normal Klein four subgroup.

The kernel of the action on the four Sylow $3$-subgroups has order
$6$ in $S_3\times A_4$ and order $3$ in the other three; it is an
isomorphism invariant. To check the asserted kernels, each Sylow $3$-subgroup
of $S_4$ or $A_4$ fixes exactly one of the four letters, with one
such subgroup for each letter. The conjugation action on these
subgroups is thus their faithful natural action on the four letters.
Also $S_4$ has trivial center, since an element commuting with
every transposition preserves every unordered pair of letters
and therefore fixes every letter. Thus $C_3\times S_4$ has center
of order $3$. The other two have trivial center: a central element
projects to the trivial center of $S_4$, hence lies in the kernel
$C_3$, and an odd permutation inverts that kernel.
Finally $D_{18}\times_{S_3}S_4$ has a cyclic Sylow $3$-subgroup
of order $9$, the pullback of a $3$-cycle subgroup along
$C_9\to C_3$. In $C_3\rtimes_{\mathrm{sgn}}S_4$ the Sylow
$3$-subgroup is $C_3\times C_3$, since a $3$-cycle acts trivially
on the kernel. This distinguishes the last two groups.
:::

<1>5. The list has exactly $50$ isomorphism classes and omits none.

::: proof
Every group has either a normal Sylow $3$-subgroup, a normal Sylow
$2$-subgroup but not a normal Sylow $3$-subgroup, or neither.
Steps <1>1, <1>3, and <1>4 classify these disjoint cases, with
$42$, $4$, and $4$ distinct classes respectively. Their sum is $50$.
:::
:::
