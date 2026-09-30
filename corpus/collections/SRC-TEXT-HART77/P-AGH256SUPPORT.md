---
schema: qual/card@1
id: P-AGH256SUPPORT
kind: problem
title: Support of a module and sections with support in a closed set
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coherent Sheaves
  - Support
  - Local Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all five parts with the retained MinerU transcription Hartshorne_Solutions_extracted.md, section 2.5, solution 5.6, and read the support and supported-subsheaf prerequisites. Checked the annihilator characterization against Stacks Project Tag 00L2; proved the torsion-subsheaf identification directly on distinguished opens.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Recall the notions of support of a section of a sheaf, support of a sheaf, and subsheaf with supports from (Ex. 1.14) and (Ex. 1.20).

(a) Let $A$ be a ring, let $M$ be an $A$-module, let $X = \Spec A$, and let $\mcf = \widetilde M$.
For any $m \in M = \Gamma(X,\mcf)$, show that $\supp m = V(\Ann m)$, where $\Ann m = \theset{a \in A \st am = 0}$.

(b) Now suppose that $A$ is noetherian and $M$ finitely generated.
Show that $\supp \mcf = V(\Ann M)$.

(c) The support of a coherent sheaf on a noetherian scheme is closed.

(d) For any ideal $\mfa \subseteq A$, define a submodule $\Gamma_\mfa(M)$ of $M$ by
$$
\Gamma_\mfa(M) = \theset{m \in M \st \mfa^n m = 0 \text{ for some } n > 0}.
$$
Assume that $A$ is noetherian, and $M$ any $A$-module.
Show that $\Gamma_\mfa(M)^\sim \cong \mch^0_Z(\mcf)$, where $Z = V(\mfa)$ and $\mcf = \widetilde M$.

(e) Let $X$ be a noetherian scheme, and let $Z$ be a closed subset.
If $\mcf$ is a quasi-coherent, respectively coherent, $\OO_X$-module, then $\mch^0_Z(\mcf)$ is also quasi-coherent, respectively coherent.
:::

::: {.hint}
For part (d), use (Ex. 1.20) and (5.8) to show a priori that $\mch^0_Z(\mcf)$ is quasi-coherent, then show that $\Gamma_\mfa(M) \cong \Gamma_Z(\mcf)$.
:::

::: {.solution}
Use the [[D-UDIVH|support]] conventions of [[P-AGH2114SUPPORT]] and the [[P-AGH2120SUPPSUBSHEAF|subsheaf of sections with support in a closed set]].
For $X=\Spec A$ and $\mcf=\widetilde M$, the stalk at $\mathfrak p$ is $M_{\mathfrak p}$ and the sections on $D(f)$ are $M_f$ [@Har10a, Proposition II.5.1].

::: pf

::: {.pf-step #s1}

For part (a), $\supp m=V(\Ann m)$.

::: pf-proof

For a prime ideal $\mathfrak p\subseteq A$, the germ $m/1$ is zero in $M_{\mathfrak p}$ exactly when there exists $s\in A\setminus\mathfrak p$ with $sm=0$.
Equivalently, $\Ann m$ is not contained in $\mathfrak p$.
Thus the germ is nonzero exactly at the primes containing $\Ann m$, proving the equality.

:::

:::

::: {.pf-step #s2}

For part (b), $\supp\mcf=V(\Ann M)$.

::: pf-proof

Choose generators $m_1,\ldots,m_r$ of $M$.
If $M_{\mathfrak p}=0$, for each $j$ there is $s_j\notin\mathfrak p$ with $s_jm_j=0$.
The product $s=\prod_j s_j$ is outside $\mathfrak p$ and annihilates all generators, hence all of $M$.
Therefore $\Ann M$ is not contained in $\mathfrak p$.
Conversely, an element of $\Ann M\setminus\mathfrak p$ becomes a unit after localization and annihilates $M_{\mathfrak p}$, forcing that module to be zero.
Consequently $M_{\mathfrak p}\ne0$ exactly when $\Ann M\subseteq\mathfrak p$.
For $M=0$ the empty product is $1$, and the same argument gives empty support.

:::

:::

::: {.pf-step #s3}

The [[D-UDIVH|support]] in part (c) is closed.

::: pf-proof

On each affine open $U=\Spec A\subseteq X$, the [[D-QNTZY|coherent]] sheaf $\mcf$ restricts to $\widetilde M$ for a finite $A$-module $M$ [@Har10a, Proposition II.5.4].
Step [](#s2){.pf-ref} shows that $\supp\mcf\cap U=V(\Ann M)$ is closed in $U$.
Thus $U\setminus\supp\mcf$ is open in $U$, hence in $X$.
The complement $X\setminus\supp\mcf$ is the union of these open subsets as $U$ runs over an affine cover, so it is open.

:::

:::

::: {.pf-step #s4}

For part (d), the inclusion $\Gamma_\mfa(M)\subseteq M$ induces an isomorphism
$$
\widetilde{\Gamma_\mfa(M)}\cong\mch_Z^0(\widetilde M).
$$

::: pf-proof

::: {.pf-step #s4-1}

The sections of $\widetilde M$ supported in $Z$ are precisely $\Gamma_\mfa(M)$.

::: pf-proof

The set $\Gamma_\mfa(M)$ is a submodule: a common power of $\mfa$ annihilates the sum of two elements annihilated by powers of $\mfa$, and scalar multiplication preserves this property.
By step [](#s1){.pf-ref} and the ideal description of closed subsets of an affine spectrum,
$$
\supp m\subseteq V(\mfa)
\quad\Longleftrightarrow\quad
V(\Ann m)\subseteq V(\mfa)
\quad\Longleftrightarrow\quad
\mfa\subseteq\sqrt{\Ann m}.
$$
If $\mfa^n m=0$, the last containment holds.
Conversely, choose generators $a_1,\ldots,a_r$ of $\mfa$ and positive integers $n_i$ such that $a_i^{n_i}m=0$.
For $N=1+\sum_i(n_i-1)$, every monomial of total degree $N$ in the $a_i$ has some exponent at least $n_i$.
These monomials generate $\mfa^N$, so $\mfa^N m=0$.
If $\mfa=0$, its first power already annihilates every element.
This proves the desired equality of section modules.

:::

:::

::: {.pf-step #s4-2}

For every $f\in A$, localization identifies
$$
\Gamma_\mfa(M)_f=\Gamma_{\mfa A_f}(M_f)
$$
as submodules of $M_f$.

::: pf-proof

Localization of the inclusion $\Gamma_\mfa(M)\subseteq M$ is injective.
An element of its source is still annihilated by a power of $\mfa A_f$, giving one containment.
For the other, let $m/f^q$ be annihilated by $(\mfa A_f)^n$.
Choose finitely many generators $b_1,\ldots,b_s$ of $\mfa^n$.
For every $j$, the equality $b_jm/f^q=0$ gives an integer $e_j\ge0$ with $f^{e_j}b_jm=0$.
Choose $e$ at least all the $e_j$.
Then $\mfa^n(f^em)=0$, and
$$
m/f^q=(f^em)/f^{q+e}\in\Gamma_\mfa(M)_f.
$$
If $\mfa^n=0$, one may take its generating list to consist of the single element zero and take $e=0$.

:::

:::

::: pf-qed

Apply step [](#s4-1){.pf-ref} over the noetherian ring $A_f$, with module $M_f$ and ideal $\mfa A_f$.
The sections of $\mch_Z^0(\widetilde M)$ on $D(f)$ are exactly $\Gamma_{\mfa A_f}(M_f)$.
By step [](#s4-2){.pf-ref}, these are also the sections of $\widetilde{\Gamma_\mfa(M)}$.
All identifications are inclusions into $M_f$ and commute with restriction.
They therefore give the asserted isomorphism on a basis, hence on $X$.

:::

:::

:::

::: {.pf-step #s5}

Part (e) follows from the affine description in step [](#s4){.pf-ref}.

::: pf-proof

For an affine open $U=\Spec A$ in $X$, write $Z\cap U=V(\mfa)$ and $\mcf|_U\cong\widetilde M$.
The [[P-AGH2120SUPPSUBSHEAF|definition of the supported subsheaf]] commutes with restriction to $U$.
Step [](#s4){.pf-ref} therefore gives
$$
\mch_Z^0(\mcf)|_U\cong\widetilde{\Gamma_\mfa(M)}.
$$
These descriptions make $\mch_Z^0(\mcf)$ [[D-QNTZY|quasi-coherent]].
If $\mcf$ is [[D-QNTZY|coherent]], then $M$ is finitely generated over the noetherian ring $A$.
Its submodule $\Gamma_\mfa(M)$ is consequently finitely generated, so the displayed associated sheaf is [[D-QNTZY|coherent]].
This proves the second assertion on an affine cover of $X$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove parts (a), (b), and (c).
Step [](#s4){.pf-ref} proves part (d), and step [](#s5){.pf-ref} proves part (e).

:::

:::

:::
