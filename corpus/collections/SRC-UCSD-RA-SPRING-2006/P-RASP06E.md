---
schema: qual/card@1
id: P-RASP06E
kind: problem
title: "Adjoint of a bounded operator and orthogonal projections"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Spring 2006 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $H$ be a Hilbert space, $P : H \to H$ a bounded linear operator, $P^* : H \to H$ its adjoint, and $\mathcal{R}(P)$, $\mathcal{N}(P)$ its range and nullspace, respectively.

(a) Show that $\mathcal{N}(P^*) = \mathcal{R}(P)^\perp$ and $\overline{\mathcal{R}(P^*)} = \mathcal{N}(P)^\perp$.

(b) Show that $\mathcal{R}(P^*)$ is closed if $\mathcal{R}(P)$ is closed.

(c) Assume that $P^2 = P$.
Show that the following are equivalent:

(i) $\mathcal{R}(P)$ is closed and $\|x - Px\| = \inf_{y \in \mathcal{R}(P)} \|x - y\|$ for every $x \in H$.

(ii) $P = P^*$.
:::

::: solution
<1>1. Identify the nullspace of the adjoint.
::: proof
For $y\in H$,
\[
y\in\mathcal N(P^*)
\iff P^*y=0
\iff \langle Px,y\rangle=0\quad\forall x\in H.
\]
The latter condition says precisely that $y$ is orthogonal to every vector in $\mathcal R(P)$. Hence
\[
\boxed{\mathcal N(P^*)=\mathcal R(P)^\perp.}
\]
Applying this identity to $P^*$ gives
\[
\mathcal N(P)=\mathcal R(P^*)^\perp.
\]
Taking orthogonal complements and using $M^{\perp\perp}=\overline M$ yields
\[
\boxed{\overline{\mathcal R(P^*)}=\mathcal N(P)^\perp.}
\]
:::

<1>2. Closed range of $P$ implies closed range of $P^*$.
::: proof
Assume $\mathcal R(P)$ is closed. The restriction
\[
P:\mathcal N(P)^\perp\longrightarrow\mathcal R(P)
\]
is a bounded bijection. By the Bounded Inverse Theorem there is $C>0$ such that
\[
\|x\|\le C\|Px\|
\qquad(x\in\mathcal N(P)^\perp).
\]

Fix $z\in\mathcal N(P)^\perp$. Define a functional $L$ on $\mathcal R(P)$ by
\[
L(Py):=\langle z,y\rangle.
\]
This is well defined: if $Py_1=Py_2$, then $y_1-y_2\in\mathcal N(P)$ and hence
\[
\langle z,y_1-y_2\rangle=0.
\]
Replacing $y$ by its orthogonal projection onto $\mathcal N(P)^\perp$ gives
\[
|L(Py)|\le \|z\|\,\|y_\perp\|
\le C\|z\|\,\|Py\|,
\]
so $L$ is bounded on the Hilbert space $\mathcal R(P)$.

By the Riesz representation theorem there is $w\in\mathcal R(P)$ such that
\[
L(v)=\langle w,v\rangle
\qquad(v\in\mathcal R(P)).
\]
Thus for every $y\in H$,
\[
\langle z,y\rangle
=L(Py)
=\langle w,Py\rangle
=\langle P^*w,y\rangle.
\]
Hence $z=P^*w\in\mathcal R(P^*)$. Therefore
\[
\mathcal N(P)^\perp\subseteq\mathcal R(P^*).
\]
Together with Step 1 this gives
\[
\mathcal R(P^*)=\mathcal N(P)^\perp,
\]
which is closed.
:::

<1>3. Self-adjoint idempotents satisfy the best-approximation property.
::: proof
Assume $P^2=P$ and $P=P^*$. Since
\[
\mathcal R(P)=\mathcal N(I-P),
\]
the range is closed. Also, for $x\in H$ and $y=Pz\in\mathcal R(P)$,
\[
\langle x-Px,y\rangle
=\langle (I-P)x,Pz\rangle
=\langle x,(I-P)Pz\rangle
=0.
\]
Thus $x-Px\perp\mathcal R(P)$. For any $y\in\mathcal R(P)$,
\[
x-y=(x-Px)+(Px-y)
\]
is an orthogonal decomposition, so
\[
\|x-y\|^2
=\|x-Px\|^2+\|Px-y\|^2
\ge\|x-Px\|^2.
\]
Hence
\[
\|x-Px\|=\inf_{y\in\mathcal R(P)}\|x-y\|.
\]
:::

<1>4. The best-approximation property forces self-adjointness.
::: proof
Assume (i). Since $Px\in\mathcal R(P)$ is a best approximation to $x$ from the closed subspace $\mathcal R(P)$, the Hilbert-space projection theorem gives
\[
x-Px\perp\mathcal R(P)
\qquad\forall x\in H.
\]
Thus
\[
\mathcal N(P)=\mathcal R(P)^\perp:
\]
indeed $x-Px\in\mathcal N(P)$ for every $x$, while every $z\in\mathcal N(P)$ satisfies $z=z-Pz\perp\mathcal R(P)$.

Therefore every $x$ has the orthogonal decomposition
\[
x=Px+(x-Px)
\in\mathcal R(P)\oplus\mathcal R(P)^\perp,
\]
and $P$ is precisely the orthogonal projection onto $\mathcal R(P)$. Orthogonal projections are self-adjoint, so
\[
\boxed{P=P^*.}
\]
:::
:::
