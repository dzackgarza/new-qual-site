---
schema: qual/card@1
id: P-AGH286INFLIFT
kind: problem
title: The infinitesimal lifting property
classification:
  areas:
  - algebraic-geometry
  topics:
  - Deformation Theory
  - Sheaves of Differentials
  - Derivations
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three steps and the commuting-map requirements with the retained Hartshorne II.8.6 transcription. Checked the split conormal criterion in Stacks Project section 10.138. The proof specifies the square-zero module actions, proves the polynomial obstruction is A-linear, and uses projectivity on the affine scheme to extend and subtract that obstruction.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
The following result is important in studying deformations of nonsingular varieties.
Let $k$ be an algebraically closed field, let $A$ be a finitely generated $k\dash$algebra such that $\Spec A$ is a nonsingular variety over $k$.
Let
$$
0 \to I \to B' \to B \to 0
$$
be an exact sequence, where $B'$ is a $k\dash$algebra and $I$ is an ideal with $I^2 = 0$.
Finally suppose given a $k\dash$algebra homomorphism $f: A \to B$.
Then there exists a $k\dash$algebra homomorphism $g: A \to B'$ lifting $f$, i.e. with $f$ equal to $g$ followed by the surjection $B' \surjects B$.
We call this the **infinitesimal lifting property for $A$**.
Prove it in several steps.

(a) First suppose that $g: A \to B'$ is a given homomorphism lifting $f$.
   If $g': A \to B'$ is another such homomorphism, show that $\theta = g - g'$ is a $k\dash$derivation of $A$ into $I$, which we can consider as an element of $\Hom_A(\Omega_{A/k}, I)$.
   Note that since $I^2 = 0$, $I$ has a natural structure of $B\dash$module and hence also of $A\dash$module.
   Conversely, for any $\theta \in \Hom_A(\Omega_{A/k}, I)$, $g' = g + \theta$ is another homomorphism lifting $f$.
   For this step you do not need the hypothesis that $\Spec A$ is nonsingular.

(b) Now let $P = k[x_1, \ldots, x_n]$ be a polynomial ring over $k$ of which $A$ is a quotient, and let $J$ be the kernel.
   Show that there does exist a homomorphism $h: P \to B'$ compatible with $f$ and with the surjections $P \surjects A$ and $B' \surjects B$, and show that $h$ induces an $A\dash$linear map $\bar h: J/J^2 \to I$.

(c) Now use the hypothesis that $\Spec A$ is nonsingular and (8.17) to obtain an exact sequence
$$
0 \to J/J^2 \to \Omega_{P/k} \tensor A \to \Omega_{A/k} \to 0
.
$$
   Show furthermore that applying $\Hom_A(\wait, I)$ gives an exact sequence
$$
0 \to \Hom_A(\Omega_{A/k}, I) \to \Hom_P(\Omega_{P/k}, I) \to \Hom_A(J/J^2, I) \to 0
.
$$
   Let $\theta \in \Hom_P(\Omega_{P/k}, I)$ be an element whose image gives $\bar h \in \Hom_A(J/J^2, I)$.
   Consider $\theta$ as a derivation of $P$ into $B'$.
   Then let $h' = h - \theta$, and show that $h'$ is a homomorphism $P \to B'$ with $h'(J) = 0$.
   Thus $h'$ induces the desired homomorphism $g: A \to B'$.
:::

::: {.solution}
Let $\rho:B'\twoheadrightarrow B$ and $\alpha:P\twoheadrightarrow A$ denote the quotient maps.
For $b\in B$ and $i\in I$, define $b\cdot i=\widetilde b\,i$ using any lift $\widetilde b\in B'$.
Two lifts differ by an element of $I$, whose product with $i$ is zero, so this gives a well-defined $B$-module structure on $I$.
Restriction of scalars along $f$ and $f\circ\alpha$ gives its $A$- and $P$-module structures.
For a homomorphism out of a module of differentials, its associated derivation always means its composite with the universal differential.

<1>1. The difference of two lifts of $f$ is a $k$-derivation $A\to I$.

::: {.proof}
Let $g,g':A\to B'$ have $\rho g=\rho g'=f$, and put $D=g-g'$.
Its values lie in $I$, it is additive, and it annihilates $k$ because the two maps are $k$-algebra homomorphisms.
For $a,b\in A$,
$$
\begin{aligned}
D(ab)
&=g(a)g(b)-g'(a)g'(b)\\
&=g(a)D(b)+g'(b)D(a)\\
&=f(a)\cdot D(b)+f(b)\cdot D(a).
\end{aligned}
$$
The last equality uses exactly the module action defined before the first step.
Thus $D$ is a $k$-derivation for the specified $A$-module structure.
The [[D-4GCH6|universal property of differentials]] identifies it with a unique member of $\Hom_A(\Omega_{A/k},I)$.
No regularity assumption on $A$ was used.
:::

<1>2. If $g$ is one lift and $D:A\to I$ is any $k$-derivation, then $g+D$ is another lift.

::: {.proof}
The map $g+D$ is additive and agrees with $g$ on $k$.
The derivation rule gives $D(1)=D(1)+D(1)$, so $D(1)=0$ and the map preserves $1$.
Since $I^2=0$,
$$
\begin{aligned}
(g(a)+D(a))(g(b)+D(b))
&=g(ab)+g(a)D(b)+g(b)D(a)\\
&=g(ab)+D(ab).
\end{aligned}
$$
It is therefore multiplicative.
Its reduction is $f$ because $D$ takes values in $I$.
Together with step <1>1, this proves both directions of (a): once a lift is chosen, all lifts are obtained uniquely by adding a derivation.
The same calculation applies to any $k$-algebra in place of $A$, in particular to $P$.
:::

<1>3. There is a polynomial lift $h:P\to B'$, and its restriction to $J$ induces an $A$-linear map $\bar h:J/J^2\to I$.

::: {.proof}
For each $x_i$, choose $b_i'\in B'$ with $\rho(b_i')=f(\alpha(x_i))$.
The universal property of the polynomial ring gives a $k$-algebra homomorphism $h$ with $h(x_i)=b_i'$.
The two maps $\rho h$ and $f\alpha$ agree on $k$ and all the variables, so they agree everywhere.
This is the required compatibility.

For $j\in J$, it follows that $h(j)\in I$.
Products of two such images vanish, so $h(J^2)=0$ and
$$
\bar h:J/J^2\longrightarrow I,\qquad [j]\longmapsto h(j)
$$
is well-defined and additive.
For $a\in A$, lift it to $p\in P$.
Then
$$
\bar h(a[j])=h(pj)=h(p)h(j)=f(a)\cdot\bar h([j]).
$$
Changing the lift $p$ changes $pj$ by an element of $J^2$, so the expression is independent of that choice.
Thus $\bar h$ is $A$-linear, proving (b).
:::

<1>4. The conormal sequence in (c) is split exact, and applying $\Hom_A(-,I)$ gives the stated short exact sequence.

::: {.proof}
The quotient $P\to A$ gives a closed immersion of the nonsingular affine variety $\Spec A$ into the nonsingular affine space $\Spec P$.
The exact conormal sequence of [@Har10a, Theorem II.8.17] is
$$
0\longrightarrow J/J^2\xrightarrow{\delta}
\Omega_{P/k}\otimes_P A\longrightarrow\Omega_{A/k}\longrightarrow0,
\qquad \delta([j])=dj\otimes1.
$$
Passing from sheaves to these modules preserves exactness because the scheme is affine.
Nonsingularity over the algebraically closed field makes the differential sheaf locally free of finite rank.
The affine locally-free/projective-module correspondence therefore makes $\Omega_{A/k}$ a finite projective $A$-module.
The surjection onto it has an $A$-linear section, so the sequence splits.

Applying $\Hom_A(-,I)$ to a split exact sequence is exact for every $A$-module $I$.
In particular, every $A$-linear map $J/J^2\to I$ extends across $\delta$: compose it with an $A$-linear retraction of $\delta$.
Finally, extension and restriction of scalars give
$$
\Hom_A(\Omega_{P/k}\otimes_P A,I)
\cong\Hom_P(\Omega_{P/k},I).
$$
Under this identification, the last map in the dual sequence sends $\theta$ to $[j]\mapsto\theta(dj)$.
Hence the short exact sequence is exactly the one requested in (c).
This is the [split conormal criterion](https://stacks.math.columbia.edu/tag/00TH) in the present affine setting; local freeness is not being treated as projectivity in a nonaffine sheaf category.
:::

<1>5. Subtracting an extending derivation gives the required lift $g:A\to B'$.

::: {.proof}
By step <1>4, choose $\theta\in\Hom_P(\Omega_{P/k},I)$ whose restriction to $J/J^2$ is $\bar h$ from step <1>3.
Let $D=\theta\circ d:P\to I$ be its associated derivation.
Viewed in $B'$, this is a derivation relative to the homomorphism $h$, since multiplication by $h(p)$ on $I$ is the prescribed action through $f\alpha(p)$.
Step <1>2, with $P$ in place of $A$ and $-D$ in place of $D$, shows that
$$
h'=h-D:P\longrightarrow B'
$$
is a $k$-algebra homomorphism with $\rho h'=f\alpha$.
For every $j\in J$,
$$
D(j)=\theta(dj)=\bar h([j])=h(j),
$$
so $h'(j)=0$.
Thus $h'$ factors through $P/J=A$, giving a $k$-algebra homomorphism $g$ with $g\alpha=h'$.
Reducing and using surjectivity of $\alpha$ gives $\rho g=f$.
This completes the construction without imposing any finiteness or smoothness assumption on $B'$ or $B$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove (a), step <1>3 proves (b), and steps <1>4--<1>5 establish both exact sequences and the lift required in (c).
:::
:::
