---
schema: qual/card@1
id: P-2HSIO
kind: problem
title: $\ker(\pi_1(A,a)\to\pi_1(X,a))\cong\pi_1(p^{-1}A,\tilde a)$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Repaired the target basepoint from $\bar a$ to the source's $\tilde a$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
---

::: problem
Suppose that X has universal cover $p : \tilde X \to X$ and let $A \subset X$ be a subspace with $p(\tilde a) = a \in A$.
Show that there is a group isomorphism
$$
\ker(\pi_1 (A, a) \to \pi_1 (X, a)) \cong \pi_1 (p\inv A, \tilde a)
.$$
:::

::: {.solution}
<1>1. The restriction
\[
q=p|_{p^{-1}(A)}:p^{-1}(A)\longrightarrow A
\]
is a covering map, with $q(\tilde a)=a$.
::: {.proof}
Let $a_0\in A$.
Choose an open neighborhood $U\subseteq X$ of $a_0$ that is evenly covered by $p$, so
\[
p^{-1}(U)=\bigsqcup_{\lambda}V_\lambda
\]
and each restriction
\[
p|_{V_\lambda}:V_\lambda\longrightarrow U
\]
is a homeomorphism.
Then $U\cap A$ is open in the subspace $A$, and
\[
q^{-1}(U\cap A)
=
\bigsqcup_\lambda\bigl(V_\lambda\cap p^{-1}(A)\bigr).
\]
Each $V_\lambda\cap p^{-1}(A)$ maps homeomorphically onto $U\cap A$ by $q$.
Thus $q$ is a covering map.
:::

<1>2. The homomorphism
\[
q_*:\pi_1(p^{-1}(A),\tilde a)\longrightarrow\pi_1(A,a)
\]
is injective.
::: {.proof}
Let $[\widetilde\alpha]\in\pi_1(p^{-1}(A),\tilde a)$ and suppose
\[
q_*[\widetilde\alpha]=1.
\]
Then $q\circ\widetilde\alpha$ is nullhomotopic in $A$ relative to its basepoint.
Lift such a nullhomotopy through the covering $q$, starting with the loop $\widetilde\alpha$.
Its terminal edge is the lift, starting at $\tilde a$, of the constant loop at $a$, hence is the constant loop at $\tilde a$.
Therefore $\widetilde\alpha$ is nullhomotopic in $p^{-1}(A)$, so $[\widetilde\alpha]=1$.
Thus $q_*$ is injective.
:::

<1>3. Let
\[
i:A\hookrightarrow X
\]
be the inclusion.
Then
\[
\operatorname{im}(q_*)\subseteq\ker(i_*).
\]
::: {.proof}
The composite $i\circ q$ is the restriction of $p$ to $p^{-1}(A)$.
If $[\widetilde\alpha]\in\pi_1(p^{-1}(A),\tilde a)$, then $\widetilde\alpha$ is also a loop in the simply connected universal cover $\widetilde X$.
Hence it is nullhomotopic in $\widetilde X$.
Applying $p$ to a nullhomotopy shows that
\[
i_*q_*[\widetilde\alpha]=1
\]
in $\pi_1(X,a)$.
Therefore every element of $\operatorname{im}(q_*)$ lies in $\ker(i_*)$.
:::

<1>4. Conversely,
\[
\ker(i_*)\subseteq\operatorname{im}(q_*).
\]
::: {.proof}
Let $[\alpha]\in\pi_1(A,a)$ satisfy
\[
i_*[\alpha]=1\in\pi_1(X,a).
\]
Let $\widetilde\alpha:[0,1]\to\widetilde X$ be the unique lift of the loop $i\circ\alpha$ with
\[
\widetilde\alpha(0)=\tilde a.
\]
Because $i\circ\alpha$ is nullhomotopic in $X$ relative to the basepoint, it is homotopic relative to endpoints to the constant loop at $a$.
Lift this homotopy through $p$ starting at $\tilde a$.
The lift of the constant loop is constant, so homotopy lifting gives
\[
\widetilde\alpha(1)=\tilde a.
\]
Thus $\widetilde\alpha$ is a loop.

Moreover,
\[
p(\widetilde\alpha(t))=\alpha(t)\in A
\]
for every $t$, so the image of $\widetilde\alpha$ lies in $p^{-1}(A)$.
It is therefore a loop in $p^{-1}(A)$ based at $\tilde a$, and
\[
q_*[\widetilde\alpha]=[\alpha].
\]
Hence $[\alpha]\in\operatorname{im}(q_*)$.
:::

<1>5. Therefore
\[
\pi_1(p^{-1}(A),\tilde a)
\cong
\ker\bigl(\pi_1(A,a)\xrightarrow{i_*}\pi_1(X,a)\bigr).
\]
::: {.proof}
By <1>2, $q_*$ is injective.
By <1>3 and <1>4,
\[
\operatorname{im}(q_*)=\ker(i_*).
\]
Thus $q_*$ is an isomorphism from $\pi_1(p^{-1}(A),\tilde a)$ onto the stated kernel.
:::
:::
