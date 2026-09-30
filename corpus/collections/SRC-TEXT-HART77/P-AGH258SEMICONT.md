---
schema: qual/card@1
id: P-AGH258SEMICONT
kind: problem
title: Semicontinuity of the fibre dimension of a coherent sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coherent Sheaves
  - Semicontinuity
  - Nakayama's Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three parts with the retained MinerU transcription Hartshorne_Solutions_extracted.md, section 2.5, solution 5.8, and Stacks Project Lemma 10.78.3. Checked the finite-cokernel shrinking argument and proved injectivity from reducedness without assuming tensor products preserve kernels.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a noetherian scheme and $\mcf$ a coherent sheaf on $X$.
Consider the function
$$
\varphi(x) = \dim_{k(x)} \mcf_x \tensor_{\OO_x} k(x),
$$
where $k(x) = \OO_x / \mfm_x$ is the residue field at $x$.
Use Nakayama's lemma to prove the following.

(a) The function $\varphi$ is upper semi-continuous, i.e. for any $n \in \ZZ$ the set $\theset{x \in X \st \varphi(x) \geq n}$ is closed.

(b) If $\mcf$ is locally free and $X$ is connected, then $\varphi$ is a constant function.

(c) Conversely, if $X$ is reduced and $\varphi$ is constant, then $\mcf$ is locally free.
:::

::: {.solution}
The fibers in the definition of $\varphi$ are finite-dimensional because $\mcf$ is [[D-QNTZY|coherent]].

::: pf

::: {.pf-step #s1}

If $\varphi(x)=r$, then $x$ has an affine neighborhood $U$ and a surjection $\OO_U^r\to\mcf|_U$.

::: pf-proof

Take an affine neighborhood $V=\Spec A$ of $x$ with $\mcf|_V\cong\widetilde M$, where $M$ is a finite $A$-module [@Har10a, Proposition II.5.4].
Let $\mathfrak p$ correspond to $x$.
Choose elements $m_1,\ldots,m_r\in M$ whose images form a basis of $M_{\mathfrak p}/\mathfrak pM_{\mathfrak p}$: each basis vector can be represented by a fraction from $M$, and multiplication by its nonzero denominator only rescales that basis vector.
By [[T-DEFNAKA|Nakayama's lemma]], their images generate $M_{\mathfrak p}$.

Let $u:A^r\to M$ send the standard basis to these elements.
The finite module $C=\operatorname{coker}u$ satisfies $C_{\mathfrak p}=0$.
For each element of a finite generating list of $C$, choose an annihilator outside $\mathfrak p$.
Their product $s\notin\mathfrak p$ annihilates $C$, so $u_s:A_s^r\to M_s$ is surjective.
The associated-sheaf map is the asserted surjection on $U=D_V(s)$.
When $r=0$, this construction gives $\mcf|_U=0$.

:::

:::

::: {.pf-step #s2}

The function $\varphi$ is upper semi-continuous, proving part (a).

::: pf-proof

Fix $n\in\ZZ$ and $x$ with $\varphi(x)=r<n$.
On the neighborhood $U$ from step [](#s1){.pf-ref}, taking the stalk at $y\in U$ and tensoring with $k(y)$ gives a surjection
$$
k(y)^r\longrightarrow\mcf_y\otimes_{\OO_{X,y}}k(y).
$$
Thus $\varphi(y)\le r<n$ throughout $U$.
It follows that $\{x:\varphi(x)<n\}$ is open, and its complement $\{x:\varphi(x)\ge n\}$ is closed.

:::

:::

::: {.pf-step #s3}

If $\mcf$ is locally free, then $\varphi$ is locally constant; connectedness makes it constant, proving part (b).

::: pf-proof

On an open set with $\mcf|_U\cong\OO_U^r$, every fiber is $k(y)^r$, so $\varphi(y)=r$ for all $y\in U$.
Hence each set $\varphi^{-1}(r)$ is open.
Its complement is the union of the other such sets and is also open, so $\varphi^{-1}(r)$ is closed as well.
If $X$ is nonempty and connected, the fiber containing any chosen point must be all of $X$.
For empty $X$ the constancy assertion is vacuous.

:::

:::

::: {.pf-step #s4}

If $X$ is reduced and $\varphi$ is constant, then $\mcf$ is locally free, proving part (c).

::: pf-proof

Write the constant value as $r$ and fix $x\in X$.
Step [](#s1){.pf-ref} gives an affine neighborhood $U=\Spec B$ and a surjective module homomorphism
$$
u:B^r\longrightarrow N
$$
whose associated sheaf is a surjection $\OO_U^r\to\mcf|_U$.
The ring $B$ is reduced because $X$ is reduced.
For each $\mathfrak q\in\Spec B$, the induced map
$$
u\otimes_B k(\mathfrak q):k(\mathfrak q)^r\longrightarrow N\otimes_B k(\mathfrak q)
$$
is surjective between vector spaces of the same finite dimension $r$, hence is an isomorphism.

Let $(b_1,\ldots,b_r)\in\ker u$.
Its image in $k(\mathfrak q)^r$ maps to zero under this isomorphism, so every $b_i$ has zero image in $k(\mathfrak q)$.
The kernel of $B\to k(\mathfrak q)$ is $\mathfrak q$, and therefore $b_i\in\mathfrak q$ for every prime $\mathfrak q$.
The intersection of all prime ideals is the nilradical, which is zero in the reduced ring $B$ [@Har10a, Chapter II, §2].
Thus every $b_i$ is zero and $u$ is injective.
It follows that $u$ is an isomorphism and $\mcf|_U\cong\OO_U^r$.
The construction applies at each point, giving local freeness.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove parts (a), (b), and (c), respectively.

:::

:::

:::

::: {.remark title="Reducedness in part (c)"}
Let $k$ be a field, put $R=k[\varepsilon]/(\varepsilon^2)$, and let $\mcf$ on $X=\Spec R$ be the sheaf associated to $R/(\varepsilon)$.
The scheme $X$ has one point, so $\varphi$ is constant with value one.
The sheaf is [[D-QNTZY|coherent]] since $R$ is noetherian and its module is finite.
It is not locally free: its stalk is nonzero and is annihilated by the nonzero element $\varepsilon$, whereas every nonzero free $R$-module has zero annihilator.
:::
