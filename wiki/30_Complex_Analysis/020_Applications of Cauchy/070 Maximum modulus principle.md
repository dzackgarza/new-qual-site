# Maximum modulus principle

:::{.theorem title="Maximum modulus principle"}
Suppose $f$ is holomorphic on $\Omega$.
If $f$ has a relative maximum at $z_0\in\Omega$, then $f$ is constant in a neighborhood of $z_0$.
If $\Omega$ is a bounded connected domain with $f$ continuous on $\Omega$ and $\bd \Omega$, then either $f$ is constant or $M \da \max_{z\in \Omega}\abs{f(z)}$ is only attained by some $z\in \bd\Omega$.
:::

:::{.proof title="by the open mapping theorem"}
Use that $z\mapsto \abs{z}$ is an open map away from $z=0$.
If $f$ is holomorphic, by the open mapping theorem it is an open map.
If $f$ attains a maximum at an interior point $z_0$, then there is some neighborhood $U\ni z_0$ where $\abs{f(U)}$ is open in $\RR$ -- but such an interval contains values larger than $\abs{f(z_0)}$, contradicting maximality at $z_0$.
:::

:::{.proof title="by the mean value theorem"}
Let $z_0\in\Omega$ and
pick any $R$ such that $\DD_R(z_0) \subseteq \Omega$.
We have
\[
f(z_0) 
&= {1\over 2\pi i}\oint_{\abs{\xi-z_0} = R} {f(\xi) \over \xi-z_0} \dz \\
&= {1\over 2\pi i}\int_0^{2\pi} {f(Re^{it} + z_0) \over Re^{it} } iRe^{it} \dt \\
&= {1\over 2\pi} \int_0^{2\pi } f(Re^{it} + z_0) \dt
,\]
so 
\[
\abs{f(z_0)} \leq {1\over 2\pi}\int_0^{2\pi }\abs{f(Re^{it} + z_0 )} \dt \leq \max_{t \in [0, 2\pi]} \abs{f(Re^{it} + z_0) }
.\]
Setting $z_R$ to be the point $Re^{it} + z_0$ that maximizes this last term, we have $f(z_0) \leq f(z_R)$.
Since this holds for all $R$, this implies $f(z_0) = f(z_R)$ for every $R$, making $f$ constant on $\DD_R(z_0)$.
By the identity principle $f$ is constant on $\Omega$.
:::

:::{.theorem title="Minimum modulus principle"}
Suppose  $f$ is holomorphic and nonvanishing on $\Omega$.
If any interior point $z_0\in \Omega^\circ$ is a relative minimum for $f$, then $f$ is constant.
If $f$ is nonconstant, then the minimum must occur on $\bd\Omega$.
:::

:::{.proof title="?"}
Suppose $f\neq 0$ on $G$.
If $f(z) = 0$ for some $z\in \bd G$, we're done, so suppose $f\neq 0$ on $\bar G$.
Then $1/f$ is holomorphic on $G$ and continuous on $\bar G$, so $\max_{z\in \bar G}\abs{1/f(z)} = \max_{z\in \bd G} \abs{1/f(z)}$.
:::

# Exercises

[[E-JTIXY]]
[[E-ZC34M]]
[[E-ZDVLE]]
[[E-J3QMJ]]
[[E-TYPSR]]
[[E-6IZL3]]
