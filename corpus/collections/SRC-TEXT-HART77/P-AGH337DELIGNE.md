---
schema: qual/card@1
id: P-AGH337DELIGNE
kind: problem
title: Deligne's formula for sections on open subsets of an affine scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quasicoherent Sheaves
  - Local Cohomology
  - Injective Modules
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both parts with the retained Hartshorne Chapter III section 3 transcription and independently examined the retained solution. Its product-of-generators correction does not preserve sections. The proof instead extends the coherent graph, removes the projection kernel by Artin-Rees, and constructs a homomorphism on an actual ideal power; it also proves injectivity of the natural colimit map.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $A$ be a noetherian ring, let $X=\Spec A$, let $\mfa \subseteq A$ be an ideal, and let $U \subseteq X$ be the open set $X-V(\mfa)$.

(a) For any $A$-module $M$, establish the following formula of Deligne:
$$
\Gamma(U, \tilde{M}) \cong \colim_n \Hom_A(\mfa^n, M).
$$

(b) Apply this in the case of an injective $A$-module $I$, to give another proof of (3.4).
:::

::: {.solution}
Use indices $n\ge1$ and transition maps
$$
\Hom_A(\mfa^n,M)\longrightarrow\Hom_A(\mfa^{n+1},M)
$$
given by restriction along $\mfa^{n+1}\subseteq\mfa^n$.
Including $n=0$ would give the same direct limit.
No finiteness hypothesis is imposed on $M$.

<1>1. There is a natural $A$-linear map
$$
\Phi:\varinjlim_n\Hom_A(\mfa^n,M)\longrightarrow\Gamma(U,\widetilde M).
$$

::: {.proof}
For every $n$, the inclusion $\widetilde{\mfa^n}\hookrightarrow\OO_X$ becomes an isomorphism on $U$.
Indeed, a prime outside $V(\mfa)$ omits some element of $\mfa$, which becomes a unit after localization, so $\mfa^nA_{\mathfrak p}=A_{\mathfrak p}$.
A homomorphism $h:\mfa^n\to M$ therefore gives, by sheafification and restriction, a map $\OO_U\to\widetilde M|_U$.
Its image of $1$ is the corresponding section $\Phi_n(h)$.

For $a\in\mfa$, its restriction to $D(a)$ is explicitly
$$
\Phi_n(h)|_{D(a)}=\frac{h(a^n)}{a^n}\in M_a.
$$
Restriction of $h$ to a larger ideal power does not change the sheaf map on $U$, since both source ideals there are identified with $\OO_U$ by inclusion.
Thus the maps $\Phi_n$ are compatible and induce $\Phi$.
Their construction commutes with homomorphisms of $M$ and preserves scalar multiplication.
:::

<1>2. The map $\Phi$ is injective.

::: {.proof}
Suppose $h:\mfa^n\to M$ gives the zero section on $U$.
Then the image module $N=\im h$ has $\widetilde N|_U=0$, because the restriction of the entire sheaf map is zero.
The module $N$ is finite: it is a quotient of the finite ideal $\mfa^n$.
By the [[P-AGH256SUPPORT|support and ideal-torsion calculation]], each of its generators is killed by a power of $\mfa$.
Choosing one exponent for the finitely many generators gives $\mfa^eN=0$ for some $e\ge1$.
Consequently
$$
h(\mfa^{n+e})=h(\mfa^e\mfa^n)=\mfa^e h(\mfa^n)=0.
$$
Thus the class of $h$ becomes zero at a later stage of the direct system and is zero in the direct limit.
This proves injectivity.
:::

<1>3. Every section $s\in\Gamma(U,\widetilde M)$ is obtained from a homomorphism $\mfa^q\to M$ for some $q\ge1$.

::: {.proof}
If $U=\varnothing$, its only section is represented by the zero homomorphism, so assume $U\ne\varnothing$.
The graph of the section is the coherent subsheaf
$$
\mathcal H_U=\{(a,as):a\in\OO_U\}
\subseteq(\OO_X\oplus\widetilde M)|_U,
$$
isomorphic to $\OO_U$ by the first projection.
The coherent-subsheaf extension theorem [[P-AGH2515EXTCOH]], part (c), gives a coherent subsheaf $\mathcal H\subseteq\OO_X\oplus\widetilde M$ restricting to this graph.
Since $X$ is affine, it corresponds to a finite submodule $F\subseteq A\oplus M$.
Write $p:F\to A$ and $v:F\to M$ for the two coordinate projections, and put $K=\ker p$ and $\mathfrak b=p(F)$.

On $U$, the first projection is an isomorphism from the graph onto $\OO_U$.
Thus $\widetilde K|_U=0$ and $\widetilde{A/\mathfrak b}|_U=0$.
Both modules are finite over the noetherian ring $A$.
The same support argument as in step <1>2 supplies integers $e,d\ge1$ with
$$
\mfa^eK=0,\qquad\mfa^d\subseteq\mathfrak b.
$$
Apply the [Artin--Rees lemma](https://stacks.math.columbia.edu/tag/00IN) to $K\subseteq F$ and $\mfa$.
For some $c\ge0$ and every $N\ge c$,
$$
\mfa^NF\cap K=\mfa^{N-c}(\mfa^cF\cap K)
\subseteq\mfa^{N-c}K.
$$
Choose $N\ge c+e$.
Then $p$ is injective on $\mfa^NF$, and its image is $\mfa^N\mathfrak b$.
Its inverse followed by the second projection is an actual module homomorphism
$$
h:\mfa^N\mathfrak b\xrightarrow{\ (p|_{\mfa^NF})^{-1}\ }\mfa^NF
\xrightarrow{v}M.
$$
Since $\mfa^{N+d}\subseteq\mfa^N\mathfrak b$, restrict $h$ to this ideal power.

On $U$, the ideal $\mfa$ is the unit ideal, so $\widetilde{\mfa^NF}|_U=\mathcal H_U$.
Under the first projection, the second projection of this graph is multiplication by the original section $s$.
The homomorphism $h$ therefore restricts to the map $a\mapsto as$ on $U$.
The inclusion of $\mfa^{N+d}$ also becomes the identity of $\OO_U$, so step <1>1 gives
$$
\Phi_{N+d}(h|_{\mfa^{N+d}})=s.
$$
This proves surjectivity without assigning potentially inconsistent values to monomial generators.
The only module to which Artin--Rees was applied was the finite graph extension $F$, not the arbitrary module $M$.
:::

<1>4. The formula in (a) is the natural isomorphism
$$
\boxed{\varinjlim_{n\ge1}\Hom_A(\mfa^n,M)\xrightarrow{\cong}\Gamma(U,\widetilde M),}
$$
with the map described in step <1>1.

::: {.proof}
Steps <1>2 and <1>3 prove bijectivity, and step <1>1 supplies linearity and naturality.
Thus the inverse has those properties as well.
:::

<1>5. For an injective $A$-module $I$, the associated sheaf $\widetilde I$ is flasque, proving (b).

::: {.proof}
Let $W\subseteq X$ be any open subset.
Write its closed complement as $V(\mathfrak b)$ for an ideal $\mathfrak b$ of $A$.
By step <1>4, a section on $W$ is represented by a homomorphism $h:\mathfrak b^n\to I$ for some $n$.
Injectivity of $I$ extends $h$ along $\mathfrak b^n\hookrightarrow A$ to $\widetilde h:A\to I$.
The element $\widetilde h(1)\in I=\Gamma(X,\widetilde I)$ restricts to the given section, because the ideal inclusion becomes an isomorphism on $W$ and step <1>1 describes exactly that restriction.
Hence every section on every open subset extends to all of $X$.
For opens $W\subseteq V\subseteq X$, restricting such a global extension to $V$ gives surjectivity of $\widetilde I(V)\to\widetilde I(W)$.
This is flasqueness and gives the asserted alternative proof of [@Har10a, Proposition III.3.4].
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 establish (a), and step <1>5 proves (b).
:::
:::

::: {.remark title="A product of generators can vanish on the open set"}
For $A=k[x,y]/(xy)$ and $\mfa=(x,y)$, the open set $U=D(x)\cup D(y)$ is nonempty, but $xy=0$ in $A$.
Multiplication by any positive power of $xy$ therefore sends the nonzero section $1\in\Gamma(U,\OO_U)$ to zero.
Thus a denominator correction using a product of all generators need not preserve a section on their union of distinguished opens.
Step <1>3 instead restricts a homomorphism to a power of the whole ideal, which is the unit ideal everywhere on $U$.
:::
