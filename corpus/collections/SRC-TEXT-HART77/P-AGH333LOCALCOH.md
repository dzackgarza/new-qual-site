---
schema: qual/card@1
id: P-AGH333LOCALCOH
kind: problem
title: Local cohomology modules of an ideal
classification:
  areas:
  - algebraic-geometry
  topics:
  - Local Cohomology
  - Derived Functors
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three parts with the retained Hartshorne Chapter III section 3 transcription. Read the ideal-torsion and supported-acyclicity prerequisites. The comparison uses sheafified injective module resolutions as flasque resolutions, and the torsion assertion is proved on cocycle representatives for arbitrary modules.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $A$ be a noetherian ring, and let $\mfa$ be an ideal of $A$.

(a) Show that $\Gamma_{\mfa}(\wait)$ (II, Ex. 5.6) is a left-exact functor from the category of $A$-modules to itself.
We denote its right derived functors, calculated in $\Mod(A)$, by $H_{\mfa}^i(\wait)$.

(b) Now let $X=\Spec A$, $Y=V(\mfa)$.
Show that for any $A$-module $M$,
$$
H_{\mfa}^i(M)=H_Y^i(X, \tilde{M}),
$$
where $H_Y^i(X, \wait)$ denotes cohomology with supports in $Y$ (Ex. 2.3).

(c) For any $i\ge0$, show that $\Gamma_{\mfa}(H_{\mfa}^i(M))=H_{\mfa}^i(M)$.
:::

::: {.solution}
For an $A$-module $M$, the [[P-AGH256SUPPORT|ideal-torsion submodule]] is
$$
\Gamma_{\mfa}(M)=\{m\in M:\mfa^n m=0\text{ for some integer }n\ge1\}.
$$
No finite-generation hypothesis is placed on $M$.

<1>1. The assignment $M\mapsto\Gamma_{\mfa}(M)$ is an additive left exact functor, proving (a).

::: {.proof}
If two elements are killed by powers $\mfa^r$ and $\mfa^s$, their sum is killed by $\mfa^{\max(r,s)}$.
Multiplying an element by a scalar in $A$ preserves any annihilating power.
Thus $\Gamma_{\mfa}(M)$ is a submodule.
An $A$-linear homomorphism sends an element killed by $\mfa^n$ to one killed by the same power, so the construction is functorial and additive.

For an exact sequence $0\to M'\xrightarrow{u}M\xrightarrow{v}M''$, the induced map on torsion submodules is injective at the left.
If $m\in\Gamma_{\mfa}(M)$ lies in $\ker v$, write $m=u(m')$.
For a power $\mfa^n$ killing $m$, injectivity of $u$ gives $\mfa^n m'=0$.
Hence $m'$ lies in $\Gamma_{\mfa}(M')$, proving exactness at the middle term.
:::

<1>2. Under $M\cong\Gamma(X,\widetilde M)$, one has a natural equality
$$
\Gamma_{\mfa}(M)=\Gamma_Y(X,\widetilde M).
$$

::: {.proof}
The support of the section corresponding to $m$ is $V(\Ann_A(m))$, by [[P-AGH256SUPPORT]], part (a).
It is contained in $V(\mfa)$ exactly when $\mfa\subseteq\sqrt{\Ann_A(m)}$.
If $\mfa^n m=0$, this containment holds.

Conversely, choose generators $a_1,\ldots,a_r$ of $\mfa$ and positive integers $n_j$ with $a_j^{n_j}m=0$.
Every monomial of total degree $N=1+\sum_j(n_j-1)$ in the generators is divisible by one of these annihilating powers.
Thus $\mfa^N m=0$.
For $\mfa=0$ the assertion holds directly, since all elements are killed by its first power and $Y=X$.
This proves equality, and its construction commutes with all module homomorphisms.
:::

<1>3. For every $i\ge0$ there is a natural $A$-linear isomorphism
$$
\boxed{H_{\mfa}^i(M)\cong H_Y^i(X,\widetilde M),}
$$
proving (b).

::: {.proof}
Choose an injective resolution $M\to I^\bullet$ in the category of $A$-modules.
The associated-sheaf functor on $\Spec A$ is exact, as can be checked by localization at every prime, so $\widetilde M\to\widetilde{I^\bullet}$ is an exact resolution.
Since $A$ is noetherian, each $\widetilde{I^q}$ is flasque [@Har10a, Proposition III.3.4].
Flasque sheaves are acyclic for sections supported in a closed subset, by [[P-AGH323SUPPORTS]], part (c).
Consequently this resolution computes the supported cohomology of $\widetilde M$.
It is not necessary that the associated sheaves be injective as abelian sheaves.

Step <1>2 identifies, term by term and compatibly with the differentials, the complexes
$$
\Gamma_{\mfa}(I^\bullet)\cong\Gamma_Y(X,\widetilde{I^\bullet}).
$$
The cohomology of the first is $H_{\mfa}^i(M)$ by definition and that of the second is $H_Y^i(X,\widetilde M)$ by the preceding acyclicity.
This gives the required isomorphism.
All maps preserve scalar multiplication, and comparison of injective resolutions makes the isomorphism natural in $M$ [@Har10a, Chapter III, §1].
:::

<1>4. Every element of $H_{\mfa}^i(M)$ is killed by some power of $\mfa$, proving (c).

::: {.proof}
Compute the group by $\Gamma_{\mfa}(I^\bullet)$ as in step <1>3.
A cohomology class has a cocycle representative $z\in\Gamma_{\mfa}(I^i)$.
By definition, some power $\mfa^n$ kills $z$ and therefore also kills its cohomology class.
Thus every element belongs to $\Gamma_{\mfa}(H_{\mfa}^i(M))$, proving equality with the whole module.
The exponent may depend on the class; a single exponent annihilating the entire cohomology module is not required.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves (a), steps <1>2--<1>3 prove (b), and step <1>4 proves (c).
:::
:::
