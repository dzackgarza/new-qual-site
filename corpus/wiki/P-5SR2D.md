---
schema: qual/card@1
id: P-5SR2D
kind: problem
title: Analyticity of $z\mapsto\overline{f(\overline{z})}$
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-reflection
  - cauchy-riemann
  - holomorphic-functions
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Prove that if $z\mapsto f(z)$ is analytic, then $z \mapsto \bar{f(\bar z)}$ is analytic.
:::

:::{.solution title="Cauchy-Riemann"}
It suffices to show that $g(z) \da \bar{f(\bar z)}$ satisfies CR.
Write $f=u+iv$, then
\[
g(x, y) \da a(x, y) + ib(x, y) = u(x, -y) -i v(x, -y)
,\]
so we want to show $a_x = b_y$ and $a_y = -b_x$.
By the chain rule,
\[
a_x &= \del_x (x\mapsto u(x, -y)) = u_x \\ 
a_y &= \del_x (y\mapsto u(x, y))\circ(y\mapsto -y) = -u_y \\ 
b_x &= \del_x(x\mapsto -v(x, -y)) = -v_x \\
b_y &= \del_x(y \mapsto - v(x, y))\circ(y\mapsto -y) = v_y
.\]
Now use CR for $f$ to write
\[
a_x &= u_x = v_y = b_y \\
a_y &= -u_y = v_x = -b_x
.\]





:::

:::{.solution title="Direct definition"}
Set $g(z) \da (f(z^*))^* \da \bar{f(\bar z)}$, we can then show $g'$ exists:
\[
\lim_{h\to 0} {g(z+h) - g(z) \over h} 
&\da \lim_{h\to 0} {f((z+h)^*)^* - f(z^*)^* \over h^{**}} \\
&= \lim_{h\to 0} {\qty{ f(z^* + h^*) - f(z^*) }^* \over h^{**}} \\
&= \lim_{h\to 0} \qty{ f(z^* + h^* ) - f(z^*) \over h^* }^* \\
&\da \qty{f'(z^*)}^*
,\]
where we've used that $w\mapsto w^*$ is continuous to commute a limit.
So this limit exists, $g$ is differentiable with $g'(z) \da \bar{f'(\bar z)}$.


:::

:::{.solution title="Power series"}
Since $f$ is analytic, take a Laurent expansion $f(z) = \sum_{k\geq 0} c_k z^k$.
Then
\[
g(z) \da (f(z^*))^*
= \qty{\sum_{k\geq 0} c_k \bar{z^k} }^* 
= \sum_{k\geq 0} \bar{c_k} z^k
,\] 
making $g$ analytic.
:::
