---
schema: qual/card@1
id: P-BERK81S-07
kind: problem
title: Evaluate a contour integral of $1/\sin(1/z)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used w=1/z. The positively oriented circle |z|=1/5 becomes the
    negatively oriented circle |w|=5, and the Jacobian reverses the sign,
    yielding the positive contour integral of 1/(w^2 sin w) on |w|=5.
    Its only poles inside are 0 and ±pi. Their residues are
    1/6,-1/pi^2,-1/pi^2, so the normalized integral is
    1/6-2/pi^2.
---

::: {.problem}
Compute
\[
\frac1{2\pi i}\int_C\frac{dz}{\sin(1/z)},
\]
where $C$ is the positively oriented circle $|z|=1/5$.
:::

::: {.solution}
<1>1. Under the change of variables
$$
w=\frac1z,
$$
the contour $C$ becomes the circle
$$
\abs w=5
$$
with negative orientation.

::: {.proof}
Parametrize
$$
z(t)=\frac15e^{it},
\qquad
0\leq t\leq2\pi.
$$
Then
$$
w(t)=\frac1{z(t)}=5e^{-it},
$$
which traverses $\abs w=5$ clockwise.
:::

<1>2. The original contour integral satisfies
$$
\int_C\frac{dz}{\sin(1/z)}
=
\int_{\abs w=5}^{+}
\frac{dw}{w^2\sin w},
$$
where the circle on the right is positively oriented.

::: {.proof}
Since
$$
z=\frac1w,
\qquad
dz=-\frac{dw}{w^2},
$$
step <1>1 gives
$$
\int_C\frac{dz}{\sin(1/z)}
=
\int_{\abs w=5}^{-}
-\frac{dw}{w^2\sin w}.
$$
Reversing the orientation removes the minus sign:
$$
\int_{\abs w=5}^{-}
-\frac{dw}{w^2\sin w}
=
\int_{\abs w=5}^{+}
\frac{dw}{w^2\sin w}.
$$
:::

<1>3. The meromorphic function
$$
F(w)=\frac1{w^2\sin w}
$$
has exactly three poles inside $\abs w<5$, at
$$
0,\quad \pi,\quad -\pi.
$$

::: {.proof}
Away from $w=0$, the poles occur at the zeros of $\sin w$, namely
$$
w=k\pi,
\qquad
k\in\ZZ.
$$
Inside $\abs w<5$, the only nonzero such points are $\pi$ and $-\pi$,
because
$$
\pi<5<2\pi.
$$
The factor $w^2$ also makes $w=0$ a pole.
:::

<1>4. The residue of $F$ at $w=\pi$ is
$$
-\frac1{\pi^2}.
$$

::: {.proof}
The zero of $\sin w$ at $\pi$ is simple, with
$$
\cos\pi=-1.
$$
Therefore
$$
\begin{aligned}
\operatorname{Res}_{w=\pi}F(w)
&=
\frac1{\pi^2}
\frac1{\cos\pi}\\
&=
-\frac1{\pi^2}.
\end{aligned}
$$
:::

<1>5. The residue of $F$ at $w=-\pi$ is
$$
-\frac1{\pi^2}.
$$

::: {.proof}
Again the zero of $\sin w$ is simple, and
$$
\cos(-\pi)=-1.
$$
Thus
$$
\operatorname{Res}_{w=-\pi}F(w)
=
\frac1{(-\pi)^2}
\frac1{\cos(-\pi)}
=
-\frac1{\pi^2}.
$$
:::

<1>6. The residue of $F$ at $w=0$ is
$$
\frac16.
$$

::: {.proof}
The Taylor expansion
$$
\sin w
=
w-\frac{w^3}{6}+O(w^5)
$$
gives
$$
\begin{aligned}
\frac1{w^2\sin w}
&=
\frac1{
w^3
\left(
1-\frac{w^2}{6}+O(w^4)
\right)
}\\
&=
\frac1{w^3}
\left(
1+\frac{w^2}{6}+O(w^4)
\right)\\
&=
\frac1{w^3}
+
\frac1{6w}
+
O(w).
\end{aligned}
$$
The coefficient of $w^{-1}$ is $1/6$.
:::

<1>7. The sum of the residues inside $\abs w=5$ is
$$
\frac16-\frac2{\pi^2}.
$$

::: {.proof}
Add the residues from steps <1>4--<1>6:
$$
\frac16-\frac1{\pi^2}-\frac1{\pi^2}
=
\frac16-\frac2{\pi^2}.
$$
:::

<1>8. The value of the requested integral is
$$
\boxed{
\frac1{2\pi i}
\int_C
\frac{dz}{\sin(1/z)}
=
\frac16-\frac2{\pi^2}.
}
$$

::: {.proof}
By steps <1>2--<1>3, the residue theorem applies to $F$ on the positively
oriented circle $\abs w=5$. Hence
$$
\frac1{2\pi i}
\int_C
\frac{dz}{\sin(1/z)}
=
\sum_{\abs a<5}\operatorname{Res}_{w=a}F(w).
$$
Step <1>7 evaluates this sum.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the requested value.
:::
:::
