---
schema: qual/card@1
id: P-AGH357AMPLENESS
kind: problem
title: Ampleness under restriction, reduction, and finite surjections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ample Sheaves
  - Proper Schemes
  - Finite Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all four parts and the cohomological hints with the retained Hartshorne Chapter III section 5 transcription and the exact scope of Proposition III.5.3. The proof retains the proper noetherian-base hypotheses, uses finite nilpotent filtrations and reduced-component filtrations, and proves finite-surjection descent without a trace or separability assumption.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ (respectively, $Y$) be proper schemes over a noetherian ring $A$.
We denote by $\mcl$ an invertible sheaf.

(a) If $\mcl$ is ample on $X$, and $Y$ is any closed subscheme of $X$, then $i^*\mcl$ is ample on $Y$, where $i:Y\to X$ is the inclusion.

(b) The sheaf $\mcl$ is ample on $X$ if and only if $\mcl_{\mathrm{red}}=\mcl\tensor\mco_{X_{\mathrm{red}}}$ is ample on $X_{\mathrm{red}}$.

(c) Suppose $X$ is reduced.
Then $\mcl$ is ample on $X$ if and only if $\mcl \tensor \mco_{X_i}$ is ample on $X_i$, for each irreducible component $X_i$ of $X$.

(d) Let $f:X\to Y$ be a finite surjective morphism, and let $\mcl$ be an invertible sheaf on $Y$.
Then $\mcl$ is ample on $Y$ if and only if $f^* \mcl$ is ample on $X$.
:::

::: {.hint}
Use Proposition III.5.3 and compare Exercises III.3.1, III.3.2, III.4.1 and III.4.2.
:::

::: {.solution}
All the schemes and closed subschemes used below are noetherian and proper over the indicated noetherian ring.
Use the cohomological criterion: an invertible sheaf $L$ on such a scheme $T$ is ample exactly when, for every coherent $F$, there is an $n_0$ with
$$
H^i(T,F\otimes L^{\otimes n})=0\qquad(i>0,\ n\ge n_0)
$$
[@Har10a, Proposition III.5.3].
Write $L^n$ for its tensor powers.
Empty schemes satisfy the conditions vacuously.

<1>1. Restriction to a closed subscheme preserves ampleness, proving (a).

::: {.proof}
Let $i:Y\hookrightarrow X$ be closed and let $F$ be coherent on $Y$.
Its direct image $i_*F$ is coherent by [[P-AGH255PUSHCOH]], since a closed immersion is finite.
For an invertible $L$ on $X$, there is an isomorphism
$$
i_*(F\otimes i^*L^n)\cong i_*F\otimes L^n.
$$
It follows by trivializing $L$ on an open cover of $X$, where the identification is the identity on the same module of sections.
Closed direct image preserves cohomology [@Har10a, Lemma III.2.10].
Hence ampleness of $L$ makes $H^i(Y,F\otimes i^*L^n)$ vanish for every $i>0$ and every sufficiently large $n$.
The criterion gives ampleness of $i^*L$.
:::

<1>2. Ampleness can be tested on the reduction, proving (b).

::: {.proof}
One implication is step <1>1 applied to $X_{\mathrm{red}}\hookrightarrow X$.
Conversely, suppose $L_{\mathrm{red}}$ is ample and let $N$ be the nilradical ideal sheaf of $X$.
It is nilpotent: on a noetherian affine chart its finitely many nilpotent ideal generators have a common bound making a sufficiently large ideal power zero, and a finite affine cover gives one exponent $e$ with $N^e=0$ globally.

For a coherent sheaf $F$, use its finite filtration $F\supseteq NF\supseteq\cdots\supseteq N^eF=0$.
Each quotient $N^jF/N^{j+1}F$ is coherent and annihilated by $N$, so is a coherent sheaf on $X_{\mathrm{red}}$ extended to $X$.
Its positive-degree cohomology after tensoring with $L^n$ vanishes for all sufficiently large $n$, by the criterion on the reduction and closed direct image.
There are only finitely many quotients, so choose one bound for all of them.
The long exact sequences of their successive extensions show, starting from $N^eF=0$, that $H^i(X,F\otimes L^n)=0$ for every $i>0$ beyond that bound.
The criterion on $X$ gives ampleness of $L$.
:::

<1>3. On a reduced scheme, ampleness can be tested on its irreducible components, proving (c).

::: {.proof}
Restriction from an ample sheaf gives the forward implication by step <1>1.
For the converse, induct on the finite number of irreducible components, all with their reduced structures.
The one-component case is the hypothesis itself; the empty case is immediate.
Let $Z$ be one component and $W$ the reduced union of the others.
Induction makes $L|_W$ ample, and $L|_Z$ is ample by assumption.

Let $I,J$ be the ideal sheaves of $Z,W$ in $X$.
Since $X$ is reduced and $Z\cup W=X$, their intersection is zero and hence $IJ=0$, as proved in [[P-AGH332COMPONENTAFFINE]], step <1>2.
For any coherent $F$, the sequence
$$
0\longrightarrow IF\longrightarrow F\longrightarrow F/IF\longrightarrow0
$$
has first term annihilated by $J$ and last term annihilated by $I$.
They are coherent sheaves on $W$ and $Z$, respectively, extended to $X$.
Their positive-degree cohomology after twisting vanishes for sufficiently large $n$ by the criterion on those two schemes.
The long exact sequence then gives the same vanishing for $F\otimes L^n$.
Applying the criterion on $X$ proves the induction step.
:::

<1>4. Pullback by a finite morphism preserves ampleness in the stated proper setting.

::: {.proof}
Let $f:X\to Y$ be finite and let $L$ be ample on $Y$.
For coherent $G$ on $X$, the sheaf $f_*G$ is coherent by [[P-AGH255PUSHCOH]].
The projection formula for an invertible sheaf, obtained by trivializing it on $Y$, gives
$$
f_*(G\otimes f^*L^n)\cong f_*G\otimes L^n.
$$
Since $f$ is affine, [[P-AGH341AFFINEMORPH]] identifies the cohomology of the left side on $Y$ with that of $G\otimes f^*L^n$ on $X$.
Ampleness of $L$ therefore gives all the eventual positive-degree vanishings on $X$.
The criterion proves that $f^*L$ is ample.
This direction does not require surjectivity.
:::

<1>5. Suppose $f:X\to Y$ is finite surjective with both schemes integral, $f^*L$ is ample, and $L$ restricts to an ample sheaf on every proper reduced closed subscheme of $Y$.
Then $L$ is ample on $Y$.

::: {.proof}
For a coherent $F$ on $Y$, the generic comparison constructed in [[P-AGH342CHEVALLEY]], parts (a) and (b), gives a coherent $G$ on $X$ and a map
$$
\beta:f_*G\longrightarrow F^{\oplus r},\qquad r=[K(X):K(Y)]>0,
$$
which is an isomorphism at the generic point of $Y$.
That construction uses a function-field basis and sheaf Hom; it does not require the schemes to be affine or the extension to be separable.
Let $K=\ker\beta$, $C=\coker\beta$ and $Q=\im\beta$.
These are coherent, and $K,C$ have proper closed support.

Each of $K,C$ is a coherent sheaf on the closed subscheme defined by its annihilator.
The reduction of that closed subscheme is a proper reduced closed subscheme of $Y$.
By hypothesis and step <1>2, the restriction of $L$ is ample on the whole annihilator subscheme, including its nilpotent structure.
Thus $H^i(Y,K\otimes L^n)$ and $H^i(Y,C\otimes L^n)$ vanish for every $i>0$ and all sufficiently large $n$.
Moreover,
$$
H^i(Y,f_*G\otimes L^n)\cong H^i(X,G\otimes f^*L^n)=0
$$
for $i>0$ and large $n$, by affine cohomology, the projection formula, and ampleness upstairs.

Choose a common bound for these three eventual vanishings.
The two exact sequences
$$
0\to K\to f_*G\to Q\to0,\qquad
0\to Q\to F^{\oplus r}\to C\to0
$$
remain exact after twisting by $L^n$.
The first makes every $H^i(Y,Q\otimes L^n)$ vanish for $i>0$, using also the vanishing of $H^{i+1}(Y,K\otimes L^n)$.
The second gives vanishing of $H^i(Y,(F\otimes L^n)^{\oplus r})$ for $i>0$.
Since $r>0$ and cohomology commutes with finite direct sums, $H^i(Y,F\otimes L^n)=0$ for every such $i$ and $n$.
The criterion for all coherent $F$ proves ampleness of $L$.
:::

<1>6. A finite surjective morphism detects ampleness, completing (d).

::: {.proof}
Assume $f^*L$ is ample and apply noetherian induction to closed subsets $T\subseteq Y$ to prove ampleness of $L|_{T_{\mathrm{red}}}$.
Suppose this is known for all proper closed subsets of a nonempty $T$.
If $T$ is reducible, its irreducible components are proper closed subsets, so the claim follows from the induction hypothesis and step <1>3.
Suppose instead that $T$ is irreducible, so $T_{\mathrm{red}}$ is integral.

The base change $X_T=X\times_Y T_{\mathrm{red}}$ is a closed subscheme of $X$ finite surjective over $T_{\mathrm{red}}$.
Its restriction of $f^*L$ is ample by step <1>1, and the same holds on its reduction and each irreducible component.
The finitely many components have closed images covering $T$; irreducibility forces one such image to be all of $T$.
Choose a component with its reduced structure and call it $Z$.
Then $Z\to T_{\mathrm{red}}$ is finite surjective between integral proper schemes, and the pullback of $L|_{T_{\mathrm{red}}}$ is ample on $Z$.
Every proper reduced closed subscheme of the target has ample restricted $L$ by the induction hypothesis.
Step <1>5 now proves ampleness on $T_{\mathrm{red}}$.

The induction gives ampleness on $Y_{\mathrm{red}}$ by taking $T=Y$.
Step <1>2 gives ampleness on $Y$ itself.
Together with step <1>4 this proves the equivalence in (d).
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove (a)--(c), and steps <1>4--<1>6 prove both directions of (d).
:::
:::
