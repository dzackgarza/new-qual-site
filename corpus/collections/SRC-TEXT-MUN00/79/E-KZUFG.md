---
schema: qual/card@1
id: E-KZUFG
kind: problem
title: Covering maps of topological groups lift the group structure
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Topological Groups
relations: []
review: draft
---

::: {.exercise}

Prove the following.

Theorem.
Let $G$ be a topological group with multiplication operation $m: G \times G \to G$ and identity element $e$.
Assume $p: \overline{G} \to G$ is a covering map.
Given $\tilde{e}$ with $p(\tilde{e}) = e$, there is a unique multiplication operation on $\overline{G}$ that makes it into a topological group such that $\tilde{e}$ is the identity element and $p$ is a homomorphism.

(a) Let $I: G \to G$ be the map $I(g) = g^{-1}$.
Show there exist unique maps $\overline{m}: \overline{G} \times \overline{G} \to \overline{G}$ and $\overline{I}: \overline{G} \to \overline{G}$ with $\overline{m}(\tilde{e} \times \tilde{e}) = \tilde{e}$ and $\overline{I}(\tilde{e}) = \tilde{e}$ such that $p \circ \overline{m} = m \circ (p \times p)$ and $p \circ \overline{I} = I \circ p$.

(b) Show the maps $\overline{G} \to \overline{G}$ given by $\tilde{g} \to \overline{m}(\tilde{e} \times \tilde{g})$ and $\tilde{g} \to \overline{m}(\tilde{g} \times \tilde{e})$ equal the identity map of $\overline{G}$.
[Hint: Use the uniqueness part of Lemma 79.1.]

(c) Show the maps $\overline{G} \to \overline{G}$ given by $\tilde{g} \to \overline{m}(\tilde{g} \times \overline{I}(\tilde{g}))$ and $\tilde{g} \to \overline{m}(\overline{I}(\tilde{g}) \times \tilde{g})$ map $\overline{G}$ to $\tilde{e}$.

(d) Show the maps $\overline{G} \times \overline{G} \times \overline{G} \to \overline{G}$ given by

$$
\tilde{g} \times \tilde{g}' \times \tilde{g}'' \to \overline{m}(\tilde{g} \times \overline{m}(\tilde{g}' \times \tilde{g}''))
$$

$$
\tilde{g} \times \tilde{g}' \times \tilde{g}'' \to \overline{m}(\overline{m}(\tilde{g} \times \tilde{g}') \times \tilde{g}'')
$$

are equal.

(e) Complete the proof.
:::

::: {.solution}
Let
\[
H=p_*\pi_1(\overline G,\tilde e)\le\pi_1(G,e).
\]
For a topological group, \(\pi_1(G,e)\) is abelian, and the multiplication map induces addition:
\[
m_*(u,v)=u+v,
\]
while inversion induces \(I_*(u)=-u\).

(a) On fundamental groups,
\[
(m\circ(p\times p))_*\pi_1(\overline G\times\overline G)
=H+H=H,
\]
and
\[
(I\circ p)_*\pi_1(\overline G)=-H=H.
\]
Thus the lifting criterion gives lifts
\[
\overline m:\overline G\times\overline G\to\overline G,
\qquad
\overline I:\overline G\to\overline G
\]
with
\[
p\overline m=m(p\times p),\qquad p\overline I=Ip,
\]
and with \(\overline m(\tilde e,\tilde e)=\tilde e\), \(\overline I(\tilde e)=\tilde e\). Uniqueness of based lifts makes these maps unique.

(b) Define
\[
L(\tilde g)=\overline m(\tilde e,\tilde g),\qquad
R(\tilde g)=\overline m(\tilde g,\tilde e).
\]
Both satisfy
\[
pL=p=pR
\]
and both send \(\tilde e\) to \(\tilde e\). The identity map of \(\overline G\) is another based lift of \(p\). By uniqueness of lifts,
\[
L=R=1_{\overline G}.
\]
So \(\tilde e\) is a two-sided identity.

(c) The maps
\[
A(\tilde g)=\overline m(\tilde g,\overline I(\tilde g)),\qquad
B(\tilde g)=\overline m(\overline I(\tilde g),\tilde g)
\]
both project to the constant map \(e\), since
\[
pA(\tilde g)=p(\tilde g)p(\tilde g)^{-1}=e,
\qquad
pB(\tilde g)=e.
\]
They both take \(\tilde e\) to \(\tilde e\). The constant map \(\tilde g\mapsto\tilde e\) is the unique based lift of the constant map to \(e\). Hence
\[
A=B\equiv\tilde e.
\]
Thus \(\overline I\) supplies two-sided inverses.

(d) Let
\[
F(\tilde g,\tilde g',\tilde g'')
=\overline m(\tilde g,\overline m(\tilde g',\tilde g'')),
\]
\[
F'(\tilde g,\tilde g',\tilde g'')
=\overline m(\overline m(\tilde g,\tilde g'),\tilde g'').
\]
Their projections are equal by associativity in \(G\):
\[
pF=p(\tilde g)\bigl(p(\tilde g')p(\tilde g'')\bigr)
=\bigl(p(\tilde g)p(\tilde g')\bigr)p(\tilde g'')=pF'.
\]
Both send \((\tilde e,\tilde e,\tilde e)\) to \(\tilde e\). By uniqueness of based lifts,
\[
F=F'.
\]
Hence \(\overline m\) is associative.

(e) Parts (b)--(d) show that \((\overline G,\overline m,\overline I,\tilde e)\) is a group. The operations are continuous because they were obtained as continuous lifts. By construction,
\[
p(\overline m(x,y))=p(x)p(y),\qquad
p(\overline I(x))=p(x)^{-1},
\]
so \(p\) is a continuous group homomorphism.

Finally, any other multiplication making \(\tilde e\) the identity and \(p\) a homomorphism would be a based lift of \(m(p\times p)\), hence would equal \(\overline m\) by uniqueness. The inverse map is then forced as well. Thus the topological-group structure is unique.
:::
