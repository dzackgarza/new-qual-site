---
schema: qual/card@1
id: P-TRIV-LA18
kind: problem
title: Rotation matrix about an axis and its trace
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 18, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the rotation by an angle θ around a line determined by a unit radius-vector ¯n with components $n _ { x } , n _ { y } , n _ { z }$

(a) Deduce the rotation matrix that performs this rotation.

(b) Relate the trace of this matrix to the angle θ.
:::

::: {.solution}
Let
$$
n=
\begin{pmatrix}
n_x\\
n_y\\
n_z
\end{pmatrix},
\qquad
\|n\|=1,
$$
and put
$$
c=\cos\theta,
\qquad
s=\sin\theta.
$$

<1>1. Every vector $v\in\mathbb R^3$ decomposes as
$$
v=v_\parallel+v_\perp,
$$
where
$$
v_\parallel=(n\cdot v)n
$$
and
$$
v_\perp=v-(n\cdot v)n.
$$

::: {.proof}
Because $n$ is a unit vector, $(n\cdot v)n$ is the orthogonal projection of
$v$ onto the rotation axis, and the difference is perpendicular to $n$.
:::

<1>2. A right-handed rotation by $\theta$ about the axis $n$ sends $v$ to
$$
Rv
=
v_\parallel
+
c,v_\perp
+
s(n\times v_\perp).
$$

::: {.proof}
The parallel component is fixed. In the oriented plane $n^\perp$, ordinary
planar rotation sends a vector $w$ to
$$
c,w+s(n\times w).
$$
Apply this to $w=v_\perp$.
:::

<1>3. Since
$$
n\times v_\parallel=0,
$$
step <1>2 becomes Rodrigues' formula
$$
Rv
=
c,v
+
(1-c)(n\cdot v)n
+
s(n\times v).
$$

::: {.proof}
Substitute
$$
v_\perp=v-v_\parallel
$$
into step <1>2 and use
$$
v_\parallel=(n\cdot v)n.
$$
:::

<1>4. Define
$$
[n]_\times
=
\begin{pmatrix}
0&-n_z&n_y\\
n_z&0&-n_x\\
-n_y&n_x&0
\end{pmatrix}.
$$
Then
$$
[n]_\times v=n\times v.
$$

::: {.proof}
This is the coordinate formula for the cross product.
:::

<1>5. The rotation matrix is
$$
\boxed{
R
=
cI
+
(1-c)nn^T
+
s[n]_\times.
}
$$

::: {.proof}
The three terms in step <1>3 are respectively the actions of
$$
cI,
\qquad
(1-c)nn^T,
\qquad
s[n]_\times.
$$
:::

<1>6. Explicitly,
$$
\boxed{
R=
\begin{pmatrix}
c+(1-c)n_x^2&(1-c)n_xn_y-sn_z&(1-c)n_xn_z+sn_y\\
(1-c)n_yn_x+sn_z&c+(1-c)n_y^2&(1-c)n_yn_z-sn_x\\
(1-c)n_zn_x-sn_y&(1-c)n_zn_y+sn_x&c+(1-c)n_z^2
\end{pmatrix}.
}
$$

::: {.proof}
Expand the matrix expression in step <1>5 using
$$
nn^T
=
\begin{pmatrix}
n_x^2&n_xn_y&n_xn_z\\
n_yn_x&n_y^2&n_yn_z\\
n_zn_x&n_zn_y&n_z^2
\end{pmatrix}
$$
and the matrix from step <1>4.
:::

<1>7. Part (a) follows.

::: {.proof}
Steps <1>5--<1>6 give the rotation matrix.
:::

<1>8. The trace is
$$
\boxed{\operatorname{Tr}R=1+2\cos\theta}.
$$

::: {.proof}
Take traces in step <1>5:
$$
\operatorname{Tr}R
=
c\operatorname{Tr}I
+
(1-c)\operatorname{Tr}(nn^T)
+
s\operatorname{Tr}[n]_\times.
$$
Now
$$
\operatorname{Tr}I=3,
\qquad
\operatorname{Tr}(nn^T)=n^Tn=1,
\qquad
\operatorname{Tr}[n]_\times=0.
$$
Therefore
$$
\operatorname{Tr}R
=
3c+(1-c)
=
1+2c.
$$
:::

<1>9. Equivalently,
$$
\boxed{
\cos\theta
=
\frac{\operatorname{Tr}R-1}{2}.
}
$$

::: {.proof}
Solve step <1>8 for $\cos\theta$.
:::

<1>10. Part (b) follows.

::: {.proof}
Steps <1>8--<1>9 give the requested relation.
:::

<1>11. Q.E.D.

::: {.proof}
Steps <1>7 and <1>10 establish parts (a) and (b), respectively.
:::
:::
