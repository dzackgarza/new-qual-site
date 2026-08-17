---
schema: qual/card@1
id: P-OC42E
kind: problem
title: The four lemma
classification:
  areas:
  - algebra
  topics:
  - exact-sequences
  - homological-algebra
  - modules
relations: []
review: draft
solved: false
---

::: problem
**Injectivity**: We have the following situation:

\begin{tikzcd}
a'                                              & a                                          & x                             & 0                                     \\
A_1 \arrow[dd, "\alpha_1", two heads] \arrow[r] & A_2 \arrow[dd, "\alpha_2", hook] \arrow[r] & A_3 \arrow[dd, "f"] \arrow[r] & A_4 \arrow[dd, "\alpha_4", two heads] \\
                                                &                                            &                               &                                       \\
B_1 \arrow[r]                                   & B_2 \arrow[r]                              & B_3 \arrow[r]                 & B_4                                   \\
0                                               & \alpha_2(a)                                & y = f(x) = 0                  & 0                                    
\end{tikzcd}

where we would like to show that $f$ is a monomorphism, i.e. that $\ker f = 0$.
So let $x\in \ker f$, so $y \definedas f(x) = 0 \in B_3$.

We will show that $x=0 \in A_3$:

- Since $y = 0 \in B_3$, applying $B_3 \to B_4$ yields $y \mapsto 0 \in B_4$ since these maps are homomorphisms and always map zero to zero.

- Pull back $0 \in B_4$ to $0 \in B_3$ along $\alpha_4$, which can be done since $\alpha_4$ is injective, giving $0 \in A_4$.

- Since this is $0$ in $A_4$, it is in the kernel of $A_3 \to A_4$, yielding some $x\in A_3$.

- By commutativity of the third square, $x\mapsto f(x)$ under $f: A_3 \to B_3$.

- Since $x\in \ker (A_3 \to A_4) = \im(A_2 \to A_3)$ by exactness, there is some $\alpha \in A_2$ such that $\alpha_2(a) = x \in A_3$.

- By injectivity of $\alpha_2$, $a$ maps to a unique element $\alpha_2(a) \in B_2$.

- By commutativity of the middle square, since $a \in A_2 \mapsto 0 \in B_3$, we must have $\alpha_2(a) \mapsto 0 f(x)$ under $B_2 \to B_3$.

- Then $\alpha_2(a) \in \ker(B_2 \to B_3) = \im (B_1 \to B_2)$, so it pulls back to some $b\in B_1$.

- By surjectivity of $\alpha_1$, $b$ pulls back to some $a' \in A_1$.

- By commutativity of square 1, $a' \mapsto a$ under $A_1 \to A_2$.

- So $a \mapsto x$ under $A_1 \to A_3$.

- But then $a \in \im(A_1 \to A_2) = \ker(A_2 \to A_3)$, so $a \mapsto 0$ under $A_1 \to A_3$.

- So $x=0$ as desired.

\newpage

**Surjectivity:** We now have this situation:

\begin{tikzcd}
A_2 \arrow[dd, "\alpha_2", two heads] \arrow[r] & A_3 \arrow[dd, "f"] \arrow[r] & A_4 \arrow[dd, "\alpha_4", two heads] \arrow[r] & A_5 \arrow[dd, "\alpha_5", hook] \\
                                                &                               &                                                 &                                  \\
B_2 \arrow[r]                                   & B_3 \arrow[r]                 & B_4 \arrow[r]                                   & B_5                             
\end{tikzcd}

Let $y \in B_3$; we want to then show that there exists an $x\in A_3$ such that $f(x) = y$.

- Apply $B_3 \to B_4$ to $y$ to obtain $y_4 \in B_4$.

- By surjectivity of $\alpha_4$, this pulls back to some $a_4 \in A_4$.

- Also by exactness of $B_3 \to B_4 \to B_5$, $y_4$ pushes forward to $0 \in B_5$

- By injectivity of $\alpha_5$, this pulls back to $0\in A_5$.

- By commutativity of the right square, $y_4 \mapsto 0$ under $A_4 \to A_5$.

- Since $a_4 \in \ker(A_4 \to A_5)$, it pulls back to some $x\in A_3$ by exactness of $A_3 \to A_4 \to A_5$.

- Then $f(x) \in B_3$, and it remains to show that $f(x) = y$.

- By commutativity of the middle square, $f(x) \mapsto y_4$ under $B_3 \to B_4$.

- Since $a \mapsto y_4$ we as well, we have $z \definedas f(x) - y \in B_3$ maps to $0\in B_4$.

- Since $z\in \ker(B_3 \to B_4)$, by exactness it pulls back to some $b_2 \in B_2$.

- By surjectivity of $\alpha_2$, this pulls back to some $a_2 \in A_2$.

- By commutativity of the first square, $a_2 \mapsto z \in B_3$.

- $a_2 \mapsto a_3 \in A_3$, where $a_3$ may not equal $x$, but $f(a_3) = z \definedas f(a) - y$.

- Then $f(a_3) = f(x) - y \implies y = f(x) - f(a_3) = f(x - a_3)$ since $f$ is a homomorphism.

- This shows that $x-a_3 \mapsto y$ under $f$, which is the element we wanted to produce.
:::
