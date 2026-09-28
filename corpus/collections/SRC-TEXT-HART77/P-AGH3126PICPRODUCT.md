---
schema: qual/card@1
id: P-AGH3126PICPRODUCT
kind: problem
title: The Picard group of a product with vanishing first cohomology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Semicontinuity
  - Picard Group
  - Products of Schemes
  - Invertible Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.12.6 and followed its instruction to use Theorem III.12.11
    in degrees 0 and 1. The proof keeps the full nonreduced base T: it derives
    local freeness and base change from the theorem itself rather than invoking
    the reduced-base Grauert corollary used in III.12.4.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be an integral projective scheme over an algebraically closed field $k$, and assume that $H^1(X, \mco_X) = 0$. Let $T$ be a connected scheme of finite type over $k$.

a. If $\mcl$ is an invertible sheaf on $X \times T$, show that the invertible sheaves $\mcl_t$ on $X = X \times \ts{t}$ are isomorphic for all closed points $t \in T$.

b. Show that $\Pic(X \times T) = \Pic X \times \Pic T$. Do not assume that $T$ is reduced.

    Hint: apply (12.11) with $i = 0, 1$ for suitable invertible sheaves on $X \times T$.

Cf. (IV, Ex. 4.10) and (V, Ex. 1.6) for examples where $\Pic(X \times T) \neq \Pic X \times \Pic T$.
:::

::: {.solution}
Let
$$
p:X\times T\longrightarrow X,
\qquad
q:X\times T\longrightarrow T
$$
be the two projections. Since \(X\) is projective over \(k\), the morphism
\(q\) is projective. It is also flat, being the base change of
\(X\to\Spec k\).

Because \(X\) is integral and projective over the algebraically closed
field \(k\),
$$
H^0(X,\mco_X)=k.
$$
By hypothesis,
$$
H^1(X,\mco_X)=0.
$$

<1>1. Local rigidity lemma. Let \(\mcf\) be an invertible sheaf on
\(X\times T\), and let \(t\in T\) be a closed point such that
$$
\mcf_t\cong\mco_X.
$$
Then there is an open neighborhood \(U\) of \(t\) and an invertible sheaf
\(\mcn_U\) on \(U\) such that
$$
\mcf|_{X\times U}\cong q_U^*\mcn_U,
$$
where \(q_U:X\times U\to U\) is the projection.

::: {.proof}
The sheaf \(\mcf\) is flat over \(T\), because it is locally isomorphic to
\(\mco_{X\times T}\), which is flat over \(T\).

Consider the degree-one base-change map at \(t\):
$$
\beta_t^1:
(R^1q_*\mcf)\tensor k(t)
\longrightarrow
H^1(X,\mcf_t).
$$
Since \(t\) is closed, \(k(t)=k\), and
$$
H^1(X,\mcf_t)
\cong
H^1(X,\mco_X)
=
0.
$$
Thus \(\beta_t^1\) is surjective. By the full
[[T-COHBC|cohomology-and-base-change theorem, Hartshorne III.12.11]],
after shrinking around \(t\), the maps \(\beta_s^1\) are isomorphisms.
In particular
$$
(R^1q_*\mcf)\tensor k(t)=0.
$$
Nakayama's lemma gives
$$
(R^1q_*\mcf)_t=0.
$$
Since \(R^1q_*\mcf\) is coherent, shrink once more so that
$$
R^1q_*\mcf=0
$$
on a neighborhood of \(t\).

The degree-one criterion in III.12.11 now implies that the degree-zero
base-change map
$$
\beta_t^0:
(q_*\mcf)\tensor k(t)
\longrightarrow
H^0(X,\mcf_t)
$$
is surjective. Applying III.12.11 in degree zero, after another shrinking
the sheaf
$$
\mcn_U=(q_U)_*(\mcf|_{X\times U})
$$
is locally free and degree-zero base change is an isomorphism. Its rank is
$$
h^0(X,\mcf_t)
=
h^0(X,\mco_X)
=
1,
$$
so \(\mcn_U\) is invertible.

There is a canonical evaluation map
$$
\epsilon:q_U^*\mcn_U\longrightarrow\mcf|_{X\times U}.
$$
On the fibre over \(t\), base change identifies it with
$$
H^0(X,\mco_X)\tensor\mco_X
\longrightarrow
\mco_X,
$$
which is an isomorphism. Let \(\mcc\) be its cokernel. The support of
\(\mcc\) is closed in \(X\times U\), and its image under the projective
morphism \(q_U\) is closed in \(U\). This image does not contain \(t\).
After deleting it, \(\epsilon\) is surjective. Both sides are invertible
sheaves, so a surjection between them is an isomorphism. This proves the
lemma.
:::

<1>2. The isomorphism class of \(\mcl_t\) is locally constant as \(t\)
ranges over the closed points of \(T\).

::: {.proof}
Fix a closed point \(t\in T\), and set
$$
\mca=\mcl_t\in\Pic X.
$$
On \(X\times T\), put
$$
\mcf=\mcl\tensor p^*(\mca^{-1}).
$$
Its fibre at \(t\) is trivial:
$$
\mcf_t
\cong
\mcl_t\tensor\mca^{-1}
\cong
\mco_X.
$$
By step <1>1, there is an open neighborhood \(U_t\) of \(t\) on which
\(\mcf\) is pulled back from \(U_t\). Therefore for every closed point
\(s\in U_t\),
$$
\mcf_s\cong\mco_X,
$$
and hence
$$
\mcl_s\cong\mca\cong\mcl_t.
$$
Thus the fibre isomorphism class is locally constant on closed points.
:::

<1>3. All the closed-point fibres \(\mcl_t\) are mutually isomorphic.
This proves part (a).

::: {.proof}
For every isomorphism class \(\alpha\in\Pic X\) that occurs among the
closed fibres, let \(V_\alpha\subseteq T\) be the union of the
neighborhoods \(U_t\) from step <1>2 over closed points \(t\) satisfying
$$
[\mcl_t]=\alpha.
$$
Each \(V_\alpha\) is open.

If \(V_\alpha\cap V_\gamma\ne\varnothing\), then this nonempty open subset
of the finite-type \(k\)-scheme \(T\) contains a closed point \(s\).
The defining property of the two neighborhoods gives
$$
[\mcl_s]=\alpha=\gamma.
$$
Hence the distinct \(V_\alpha\) are pairwise disjoint.

Their union contains every closed point of \(T\). Its complement is a
closed subset with no closed points. Since a finite-type scheme over a
field is Jacobson, that complement is empty. Thus the \(V_\alpha\) form a
disjoint open covering of \(T\). Because \(T\) is connected, only one of
them is nonempty. Therefore
$$
\mcl_t\cong\mcl_s
$$
for all closed points \(s,t\in T\), proving (a).
:::

<1>4. Suppose an invertible sheaf \(\mcf\) on \(X\times T\) satisfies
$$
\mcf_t\cong\mco_X
$$
for every closed point \(t\in T\). Then there is an invertible sheaf
\(\mcn\) on \(T\) such that
$$
\mcf\cong q^*\mcn.
$$

::: {.proof}
Set
$$
\mcn=q_*\mcf.
$$
Fix a closed point \(t\in T\). The same III.12.11 argument as in step
<1>1 applies because
$$
H^0(X,\mcf_t)=k,
\qquad
H^1(X,\mcf_t)=0.
$$
It gives an open neighborhood \(U_t\) on which \(\mcn\) is locally free
of rank \(1\), and on which degree-zero base change is an isomorphism.

The union of these \(U_t\) contains every closed point of \(T\). The
non-locally-free locus of the coherent sheaf \(\mcn\) is closed; if it
were nonempty, it would contain a closed point. Hence \(\mcn\) is
invertible on all of \(T\).

Now consider the global evaluation map
$$
\epsilon:q^*\mcn\longrightarrow\mcf.
$$
For every closed \(t\), degree-zero base change identifies its restriction
to \(X\times\{t\}\) with
$$
H^0(X,\mco_X)\tensor\mco_X
\longrightarrow
\mco_X,
$$
so it is an isomorphism on every closed fibre.

Let \(\mcc=\operatorname{coker}(\epsilon)\). If
\(\operatorname{Supp}\mcc\) were nonempty, then, being a closed subset of
the finite-type \(k\)-scheme \(X\times T\), it would contain a closed
point \((x,t)\). Its image \(t\) is then a closed point of \(T\), but the
restriction of \(\epsilon\) to that fibre is surjective, a contradiction.
Thus \(\mcc=0\), so \(\epsilon\) is surjective. Since its source and target
are invertible sheaves, it is an isomorphism:
$$
\mcf\cong q^*\mcn.
$$
This argument used III.12.11 and nowhere assumed that \(T\) is reduced.
:::

<1>5. Every invertible sheaf on \(X\times T\) is a tensor product of
pullbacks from the two factors.

::: {.proof}
Let \(\mcl\) be invertible on \(X\times T\), and choose a closed point
\(t_0\in T\). Put
$$
\mca=\mcl_{t_0}\in\Pic X
$$
and
$$
\mcf=\mcl\tensor p^*(\mca^{-1}).
$$
By part (a), for every closed \(t\),
$$
\mcl_t\cong\mcl_{t_0}=\mca,
$$
hence
$$
\mcf_t\cong\mco_X.
$$
Step <1>4 supplies an invertible sheaf \(\mcn\) on \(T\) with
$$
\mcf\cong q^*\mcn.
$$
Therefore
$$
\boxed{\mcl\cong p^*\mca\tensor q^*\mcn}.
$$
This proves surjectivity of the natural homomorphism
$$
\Phi:\Pic X\times\Pic T\longrightarrow\Pic(X\times T),
\qquad
([\mca],[\mcn])
\longmapsto
[p^*\mca\tensor q^*\mcn].
$$
:::

<1>6. The homomorphism \(\Phi\) is injective.

::: {.proof}
Suppose
$$
p^*\mca\tensor q^*\mcn\cong\mco_{X\times T}.
$$
Restrict to the fibre over any closed point \(t\in T\). The restriction
of \(q^*\mcn\) is a trivial line bundle, so
$$
\mca\cong\mco_X.
$$
Thus
$$
q^*\mcn\cong\mco_{X\times T}.
$$

Choose a closed point \(x\in X\). Since \(k\) is algebraically closed,
\(x\) is \(k\)-rational. It defines a section
$$
s_x:T\longrightarrow X\times T,
\qquad
t\longmapsto(x,t)
$$
of \(q\). Pulling the last isomorphism back by \(s_x\) gives
$$
\mcn\cong\mco_T.
$$
Hence the kernel of \(\Phi\) is trivial.
:::

<1>7. Therefore
$$
\boxed{\Pic(X\times T)\cong\Pic X\times\Pic T}.
$$

::: {.proof}
Step <1>5 proves surjectivity of \(\Phi\), and step <1>6 proves
injectivity. This proves part (b), including the case of nonreduced
connected \(T\).
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove part (a), and steps <1>4--<1>7 prove part (b).
:::
:::
