# Review of Probability Theory

Arian Maleki and Tom Do

Stanford University

Probability theory is the study of uncertainty. Through this class, we will be relying on concepts from probability theory for deriving machine learning algorithms. These notes attempt to cover the basics of probability theory at a level appropriate for CS 229. The mathematical theory of probability is very sophisticated, and delves into a branch of analysis known as measure theory. In these notes, we provide a basic treatment of probability that does not address these finer details.

## 1 Elements of probability

In order to define a probability on a set we need a few basic elements,

• Sample space Ω: The set of all the outcomes of a random experiment. Here, each outcome $\omega \in \Omega$ can be thought of as a complete description of the state of the real world at the end of the experiment.

• Set of events (or event space) $\mathcal { F } \colon \mathbf { A }$ set whose elements $A \in { \mathcal { F } }$ (called events) are subsets of $\Omega ( { \mathrm { i . e . , } } A \subseteq \Omega$ is a collection of possible outcomes of an experiment).1.

• Probability measure: A function $P : \mathcal { F }  \mathbb { R }$ that satisfies the following properties,

$P ( A ) \geq 0 .$ , for all $A \in { \mathcal { F } }$

$P ( \Omega ) = 1$

$\mathrm { I f } \ A _ { 1 } , A _ { 2 } , . . .$ . are disjoint events $( \mathrm { i . e . , } A _ { i } \cap A _ { j } = \emptyset$ whenever $i \neq j )$ , then

$$
P ( \cup _ { i } A _ { i } ) = \sum _ { i } P ( A _ { i } )
$$

These three properties are called the Axioms of Probability.

Example: Consider the event of tossing a six-sided die. The sample space is $\Omega = \{ 1 , 2 , 3 , 4 , 5 , 6 \}$ We can define different event spaces on this sample space. For example, the simplest event space is the trivial event space ${ \mathcal F } = \bar { \{ \emptyset , \Omega \} }$ . Another event space is the set of all subsets of Ω. For the first event space, the unique probability measure satisfying the requirements above is given by $P ( \emptyset ) = 0 , P ( \Omega ) = 1$ . For the second event space, one valid probability measure is to assign the probability of each set in the event space to be $\mathit { \Pi } _ { \overline { { 6 } } } ^ { - }$ where i is the number of elements of that set; for example, $\begin{array} { r } { P ( \{ 1 , 2 , 3 , 4 \} ) = \frac { 4 } { 6 } } \end{array}$ and $\begin{array} { r } { P ( \{ 1 , 2 , 3 \} ) = \frac { 3 } { 6 } } \end{array}$

Properties:

$$
\bullet \ \operatorname { I f } A \subseteq B \Longrightarrow P ( A ) \leq P ( B ) .
$$

$$
\cdot \ P ( A \cap B ) \leq \operatorname* { m i n } ( P ( A ) , P ( B ) ) .
$$

- (Union Bound) $P ( A \cup B ) \leq P ( A ) + P ( B )$

$$
\mathbf { \partial } \cdot \ P ( \Omega \setminus A ) = 1 - P ( A ) .
$$

- (Law of Total Probability) If $A _ { 1 } , \ldots , A _ { k }$ are a set of disjoint events such that $\cup _ { i = 1 } ^ { k } A _ { i } = \Omega$ , then $\begin{array} { r } { \sum _ { i = 1 } ^ { k } P ( A _ { k } ) = 1 } \end{array}$

1F should satisfy three properties: $\left( 1 \right) \varnothing \in { \mathcal { F } } ; \left( 2 \right) A \in { \mathcal { F } } \Longrightarrow \Omega \setminus A \in { \mathcal { F } } ;$ and (3) $A _ { 1 } , A _ { 2 } , \ldots \in { \mathcal { F } } \Longrightarrow$ $\cup _ { i } A _ { i } \in { \mathcal { F } } .$

## 1.1 Conditional probability and independence

Let B be an event with non-zero probability. The conditional probability of any event A given $B$ is defined as,

$$
P ( A | B ) \triangleq { \frac { P ( A \cap B ) } { P ( B ) } }
$$

In other words, $P ( A | B )$ is the probability measure of the event A after observing the occurrence of event B. Two events are called independent if and only if $P ( A \cap B ) = P ( A ) P ( { \bar { B } } )$ (or equivalently, $P ( A | B ) = P ( A ) )$ . Therefore, independence is equivalent to saying that observing B does not have any effect on the probability of A.

## 2 Random variables

Consider an experiment in which we flip 10 coins, and we want to know the number of coins that come up heads. Here, the elements of the sample space Ω are 10-length sequences of heads and tails. For example, we might have $w _ { 0 } = \langle H , H , \bar { T } , \bar { H _ { , } } T , H , H , T , T , \bar { T ( } \subseteq \Omega$ . However, in practice, we usually do not care about the probability of obtaining any particular sequence of heads and tails. Instead we usually care about real-valued functions of outcomes, such as the number of heads that appear among our 10 tosses, or the length of the longest run of tails. These functions, under some technical conditions, are known as random variables.

More formally, a random variable X is a function $X : \Omega \longrightarrow \mathbb { R } . ^ { 2 }$ Typically, we will denote random variables using upper case letters $X ( \omega )$ or more simply X (where the dependence on the random outcome $\omega$ is implied). We will denote the value that a random variable may take on using lower case letters x.

Example: In our experiment above, suppose that $X ( \omega )$ is the number of heads which occur in the sequence of tosses $\omega .$ Given that only 10 coins are tossed, $X ( \omega )$ can take only a finite number of values, so it is known as a discrete random variable. Here, the probability of the set associated with a random variable X taking on some specific value k is

$$
P ( X = k ) : = P ( \{ \omega : X ( \omega ) = k \} ) .
$$

Example: Suppose that $X ( \omega )$ is a random variable indicating the amount of time it takes for a radioactive particle to decay. In this case, $X ( \omega )$ takes on a infinite number of possible values, so it is called a continuous random variable. We denote the probability that X takes on a value between two real constants a and b (where $a < b )$ as

$$
P ( a \leq X \leq b ) : = P ( \{ \omega : a \leq X ( \omega ) \leq b \} ) .
$$

## 2.1 Cumulative distribution functions

In order to specify the probability measures used when dealing with random variables, it is often convenient to specify alternative functions (CDFs, PDFs, and PMFs) from which the probability measure governing an experiment immediately follows. In this section and the next two sections, we describe each of these types of functions in turn.

A cumulative distribution function (CDF) is a function $F _ { X } : \mathbb { R } \to [ 0 , 1 ]$ which specifies a probability measure as,

$$
F _ { X } ( x ) \triangleq P ( X \leq x ) .\tag{1}
$$

By using this function one can calculate the probability of any event in $\mathcal { F } . ^ { 3 }$ Figure ?? shows a sample CDF function.

## Properties:

<!-- image-->  
Figure 1: A cumulative distribution function (CDF).

$$
\mathbf { \partial } \cdot \ 0 \leq F _ { X } ( x ) \leq 1 .
$$

$$
\begin{array} { r } { \mathbf { \nabla } - \operatorname* { l i m } _ { x  - \infty } F _ { X } ( x ) = 0 . } \end{array}
$$

$$
\begin{array} { r } { \mathbf { \nabla } \cdot \operatorname* { l i m } _ { x  \infty } F _ { X } ( x ) = 1 . } \end{array}
$$

$$
\bullet \ x \leq y \Longrightarrow F _ { X } ( x ) \leq F _ { X } ( y ) .
$$

## 2.2 Probability mass functions

When a random variable X takes on a finite set of possible values (i.e., X is a discrete random variable), a simpler way to represent the probability measure associated with a random variable is to directly specify the probability of each value that the random variable can assume. In particular, a probability mass function (PMF) is a function $p _ { X } : \Omega \to$ R such that

$$
p _ { X } ( x ) \triangleq P ( X = x ) .
$$

In the case of discrete random variable, we use the notation $V a l ( X )$ for the set of possible values that the random variable X may assume. For example, if X(ω) is a random variable indicating the number of heads out of ten tosses of coin, then $V a l ( X ) = \{ 0 , 1 , 2 , \dots , 1 0 \}$ •

## Properties:

$$
\mathbf { \partial } \cdot 0 \leq p _ { X } ( x ) \leq 1 .
$$

$$
\begin{array} { r } { - \sum _ { x \in V a l ( X ) } p _ { X } ( x ) = 1 . } \end{array}
$$

$$
\begin{array} { r } { \mathbf { \partial } \cdot \sum _ { x \in A } p _ { X } ( x ) = P ( X \in A ) . } \end{array}
$$

## 2.3 Probability density functions

For some continuous random variables, the cumulative distribution function $F _ { X } ( x )$ is differentiable everywhere. In these cases, we define the Probability Density Function or PDF as the derivative of the CDF, i.e.,

$$
f _ { X } ( x ) \triangleq { \frac { d F _ { X } ( x ) } { d x } } .\tag{2}
$$

Note here, that the PDF for a continuous random variable may not always exist (i.e., if $F _ { X } ( x )$ is not differentiable everywhere).

According to the properties of differentiation, for very small $\Delta x .$

$$
P ( x \leq X \leq x + \Delta x ) \approx f _ { X } ( x ) \Delta x .\tag{3}
$$

Both CDFs and PDFs (when they exist!) can be used for calculating the probabilities of different events. But it should be emphasized that the value of PDF at any given point x is not the probability

of that event, $\mathrm { i . e . , } f _ { X } ( x ) \not = P ( X = x )$ . For example, $f _ { X } ( x )$ can take on values larger than one (but the integral of $f _ { X } ( x )$ over any subset of R will be at most one).

## Properties:

$f _ { X } ( x ) \geq 0$

$\textstyle \int _ { - \infty } ^ { \infty } f _ { X } ( x ) = 1 .$

- R ∈ fX (x)dx = P (X ∈ A).

## 2.4 Expectation

Suppose that X is a discrete random variable with PMF $p _ { X } ( x )$ and $g : \mathbb { R } \longrightarrow \mathbb { R }$ is an arbitrary function. In this case, $g ( X )$ can be considered a random variable, and we define the expectation or expected value of $g ( X )$ as

$$
E [ g ( X ) ] \triangleq \sum _ { x \in V a l ( X ) } g ( x ) p _ { X } ( x ) .
$$

If X is a continuous random variable with PDF $f _ { X } ( x )$ , then the expected value of $g ( X )$ is defined as,

$$
E [ g ( X ) ] \triangleq \int _ { - \infty } ^ { \infty } g ( x ) f _ { X } ( x ) d x .
$$

Intuitively, the expectation of $g ( X )$ can be thought of as a “weighted average” of the values that $g ( x )$ can taken on for different values of x, where the weights are given by $p _ { X } ( x )$ or $f _ { X } ( x )$ . As a special case of the above, note that the expectation, $E [ X ]$ of a random variable itself is found by letting $g ( x ) = x ;$ this is also known as the mean of the random variable X.

## Properties:

$E [ a ] = a$ for any constant $a \in \mathbb { R }$

$E [ a f ( X ) ] = a E [ f ( X ) ]$ for any constant $a \in \mathbb { R }$

- (Linearity of Expectation) $E [ f ( X ) + g ( X ) ] = E [ f ( X ) ] + E [ g ( X ) ]$

- For a discrete random variable X, $E [ 1 \{ X = k \} ] = P ( X = k )$

## 2.5 Variance

The variance of a random variable X is a measure of how concentrated the distribution of a random variable X is around its mean. Formally, the variance of a random variable X is defined as

$$
V a r [ X ] \triangleq E [ ( X - E ( X ) ) ^ { 2 } ]
$$

Using the properties in the previous section, we can derive an alternate expression for the variance:

$$
\begin{array} { l l l } { { E [ ( X - E [ X ] ) ^ { 2 } ] } } & { { = } } & { { E [ X ^ { 2 } - 2 E [ X ] X + E [ X ] ^ { 2 } ] } } \\ { { } } & { { = } } & { { E [ X ^ { 2 } ] - 2 E [ X ] E [ X ] + E [ X ] ^ { 2 } } } \\ { { } } & { { = } } & { { E [ X ^ { 2 } ] - E [ X ] ^ { 2 } , } } \end{array}
$$

where the second equality follows from linearity of expectations and the fact that $E [ X ]$ is actually a constant with respect to the outer expectation.

## Properties:

$V a r [ a ] = 0$ for any constant $a \in \mathbb { R }$

$\ . \ V a r [ a f ( X ) ] = a ^ { 2 } V a r [ f ( X ) ]$ for any constant $a \in \mathbb { R }$

Example Calculate the mean and the variance of the uniform random variable X with PDF $f _ { X } ( x ) =$ 1, $\forall x \in [ 0 , 1 ]$ , 0 elsewhere.

$$
E [ X ] = \int _ { - \infty } ^ { \infty } x f _ { X } ( x ) d x = \int _ { 0 } ^ { 1 } x d x = { \frac { 1 } { 2 } } .
$$

$$
E [ X ^ { 2 } ] = \int _ { - \infty } ^ { \infty } x ^ { 2 } f _ { X } ( x ) d x = \int _ { 0 } ^ { 1 } x ^ { 2 } d x = { \frac { 1 } { 3 } } .
$$

$$
V a r [ X ] = E [ X ^ { 2 } ] - E [ X ] ^ { 2 } = \frac { 1 } { 3 } - \frac { 1 } { 4 } = \frac { 1 } { 1 2 } .
$$

Example: Suppose that $g ( x ) = 1 \{ x \in A \}$ for some subset $A \subseteq \Omega$ . What is $E [ g ( X ) ] \mathcal { ! }$ Discrete case:

$$
E [ g ( X ) ] = \sum _ { x \in V a l ( X ) } 1 \{ x \in A \} P _ { X } ( x ) d x = \sum _ { x \in A } P _ { X } ( x ) d x = P ( x \in A ) .
$$

Continuous case:

$$
E [ g ( X ) ] = \int _ { - \infty } ^ { \infty } 1 \{ x \in A \} f _ { X } ( x ) d x = \int _ { x \in A } f _ { X } ( x ) d x = P ( x \in A ) .
$$

## 2.6 Some common random variables

## Discrete random variables

• X ∼ Bernoulli(p) (where $0 \leq p \leq 1 )$ : one if a coin with heads probability p comes up heads, zero otherwise.

$$
p ( x ) = { \left\{ \begin{array} { l l } { p } & { { \mathrm { i f ~ } } p = 1 } \\ { 1 - p } & { { \mathrm { i f ~ } } p = 0 } \end{array} \right. }
$$

$X \sim B i n o m i a l ( n , p )$ (where $0 \leq p \leq 1 )$ : the number of heads in n independent flips of a coin with heads probability p.

$$
p ( x ) = { \binom { n } { x } } p ^ { x } ( 1 - p ) ^ { n - x }
$$

$X \sim G e o m e t r i c ( p )$ (where $p > 0 )$ : the number of flips of a coin with heads probability p until the first heads.

$$
p ( x ) = p ( 1 - p ) ^ { x - 1 }
$$

• $X \sim P o i s s o n ( \lambda )$ (where $\lambda > 0 ) \colon$ a probability distribution over the nonnegative integers used for modeling the frequency of rare events.

$$
p ( x ) = e ^ { - \lambda } \frac { \lambda ^ { x } } { x ! }
$$

## Continuous random variables

• X ∼ Uniform(a, b) (where $a < b )$ : equal probability density to every value between a and b on the real line.

$$
f ( x ) = { \left\{ \begin{array} { l l } { { \frac { 1 } { b - a } } } & { { \mathrm { i f ~ } } a \leq x \leq b } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

• X ∼ Exponential(λ) (where $\lambda > 0 )$ : decaying probability density over the nonnegative reals.

$$
f ( x ) = { \left\{ \begin{array} { l l } { \lambda e ^ { - \lambda x } } & { { \mathrm { i f ~ } } x \geq 0 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

$X \sim N o r m a l ( \mu , \sigma ^ { 2 } )$ : also known as the Gaussian distribution

$$
f ( x ) = { \frac { 1 } { \sqrt { 2 \pi } \sigma } } e ^ { - { \frac { 1 } { 2 \sigma ^ { 2 } } } ( x - \mu ) ^ { 2 } }
$$

<!-- image-->  
Figure 2: PDF and CDF of a couple of random variables.

The shape of the PDFs and CDFs of some of these random variables are shown in Figure ??.   
The following table is the summary of some of the properties of these distributions.

<table><tr><td rowspan=1 colspan=1>Distribution</td><td rowspan=1 colspan=1>PDF or PMF</td><td rowspan=1 colspan=1>Mean</td><td rowspan=1 colspan=1>Variance</td></tr><tr><td rowspan=1 colspan=1> $B e r n o u l l i ( p )$ </td><td rowspan=1 colspan=1>p,       $\mathrm { i f } \ x = 1$ 1 − p, if $x = 0 .$ </td><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1> $p ( 1 - p )$ </td></tr><tr><td rowspan=1 colspan=1> $\overline { { B i n o m i a l ( n , p ) } }$ </td><td rowspan=1 colspan=1> $\textstyle { \binom { n } { k } } p ^ { k } ( 1 - p ) ^ { n - k } { \mathrm { ~ f o r ~ } } 0 \leq k \leq n$ </td><td rowspan=1 colspan=1>np</td><td rowspan=1 colspan=1> $n p q$ </td></tr><tr><td rowspan=1 colspan=1> $G e o m e t r i c ( p )$ </td><td rowspan=1 colspan=1> $\overline { { p ( 1 - p ) ^ { k - 1 } } }$  for k = 1, 2, . . .</td><td rowspan=1 colspan=1>HI</td><td rowspan=1 colspan=1> $\underline { { \tau - p } }$ p2</td></tr><tr><td rowspan=1 colspan=1> $P o i s s o n ( \lambda )$ </td><td rowspan=1 colspan=1> $\overline { { e ^ { - \lambda } \lambda ^ { x } / x ! } }$  for k = 1, 2, . . .</td><td rowspan=1 colspan=1>λ</td><td rowspan=1 colspan=1>λ</td></tr><tr><td rowspan=1 colspan=1> $U n i f o r m ( a , b )$ </td><td rowspan=1 colspan=1> $\frac { 1 } { b - a } \forall x \in ( a , b )$ </td><td rowspan=1 colspan=1> ${ \frac { a + b } { 2 } } $ </td><td rowspan=1 colspan=1> $\frac { ( b - a ) ^ { 2 } } { 1 2 }$ </td></tr><tr><td rowspan=1 colspan=1> $G a u s s i a n ( \mu , \sigma ^ { 2 } )$ </td><td rowspan=1 colspan=1> $\frac { 1 } { \sigma \sqrt { \gamma _ { \pi } } } e ^ { - \frac { ( x - \mu ) ^ { 2 } } { 2 \sigma ^ { 2 } } }$ </td><td rowspan=1 colspan=1>µ</td><td rowspan=1 colspan=1> $\sigma ^ { 2 }$ </td></tr><tr><td rowspan=1 colspan=1> $\overline { { E x p o n e n t i a l ( \lambda ) } }$ </td><td rowspan=1 colspan=1> $\overline { { { \lambda e ^ { - \lambda x } } \ { x \geq 0 , \lambda > 0 } } }$ </td><td rowspan=1 colspan=1> $\begin{array} { l } { { \underline { { { \mathbb { T } } } } } } \\ { { { \overline { { \lambda } } } } } \end{array}$ </td><td rowspan=1 colspan=1> $\frac { 1 } { \lambda ^ { 2 } }$ </td></tr></table>

## 3 Two random variables

Thus far, we have considered single random variables. In many situations, however, there may be more than one quantity that we are interested in knowing during a random experiment. For instance, in an experiment where we flip a coin ten times, we may care about both $\begin{array} { r l } { X ( \omega ) } & { { } = } \end{array}$ the number of heads that come up as well as $\begin{array} { r l } { Y ( \omega ) } & { { } = } \end{array}$ the length of the longest run of consecutive heads. In this section, we consider the setting of two random variables.

## 3.1 Joint and marginal distributions

Suppose that we have two random variables X and Y . One way to work with these two random variables is to consider each of them separately. If we do that we will only need $F _ { X } ( x )$ and $F _ { Y } ( y )$ But if we want to know about the values that X and Y assume simultaneously during outcomes of a random experiment, we require a more complicated structure known as the joint cumulative distribution function of X and Y , defined by

$$
F _ { X Y } ( x , y ) = P ( X \leq x , Y \leq y )
$$

It can be shown that by knowing the joint cumulative distribution function, the probability of any event involving X and Y can be calculated.

The joint CDF $F _ { X Y } ( x , y )$ and the joint distribution functions $F _ { X } ( x )$ and $F _ { Y } ( y )$ of each variable separately are related by

$$
\begin{array} { r c l } { F _ { X } ( x ) } & { = } & { \underset { y  \infty } { \mathrm { l i m } } F _ { X Y } ( x , y ) d y } \\ { F _ { Y } ( y ) } & { = } & { \underset { x  \infty } { \mathrm { l i m } } F _ { X Y } ( x , y ) d x . } \end{array}
$$

Here, we call $F _ { X } ( x )$ and $F _ { Y } ( y )$ the marginal cumulative distribution functions of $F _ { X Y } ( x , y )$ Properties:

$$
\mathbf { \partial } \cdot \mathbf { 0 } \leq F _ { X Y } ( x , y ) \leq 1 .
$$

- limx,y→∞ FXY (x, y) = 1.

$$
\begin{array} { r } { \mathbf { \nabla } \cdot \ \operatorname* { l i m } _ { x , y \to - \infty } F _ { X Y } ( x , y ) = 0 . } \end{array}
$$

$$
\begin{array} { r } { \bullet \ F _ { X } ( x ) = \operatorname* { l i m } _ { y  \infty } F _ { X Y } ( x , y ) . } \end{array}
$$

## 3.2 Joint and marginal probability mass functions

If X and Y are discrete random variables, then the joint probability mass function $p _ { X Y } : \mathbb { R } \times \mathbb { R } $ [0, 1] is defined by

$$
p _ { X Y } ( x , y ) = P ( X = x , Y = y ) .
$$

Here, $0 \le P _ { X Y } ( x , y ) \le 1$ for all $x , y ,$ , and $\begin{array} { r } { \sum _ { x \in V a l ( X ) } \sum _ { y \in V a l ( Y ) } P _ { X Y } ( x , y ) = 1 . } \end{array}$

How does the joint PMF over two variables relate to the probability mass function for each variable separately? It turns out that

$$
p _ { X } ( x ) = \sum _ { y } p _ { X Y } ( x , y ) .
$$

and similarly for $p _ { Y } ( y )$ . In this case, we refer to $p _ { X } ( x )$ as the marginal probability mass function of X. In statistics, the process of forming the marginal distribution with respect to one variable by summing out the other variable is often known as “marginalization.”

## 3.3 Joint and marginal probability density functions

Let X and Y be two continuous random variables with joint distribution function $F _ { X Y }$ . In the case that $F _ { X Y } ( x , y )$ is everywhere differentiable in both x and y, then we can define the joint probability density function,

$$
f _ { X Y } ( x , y ) = \frac { \partial ^ { 2 } F _ { X Y } ( x , y ) } { \partial x \partial y } .
$$

Like in the single-dimensional case, $f _ { X Y } ( x , y ) \neq P ( X = x , Y = y )$ , but rather

$$
\iiint _ { x \in A } f _ { X Y } ( x , y ) d x d y = P ( ( X , Y ) \in A ) .
$$

Note that the values of the probability density function $f _ { X Y } ( x , y )$ are always nonnegative, but they may be greater than 1. Nonetheless, it must be the case that $\begin{array} { r } { \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } f _ { X Y } ( x , y ) = 1 } \end{array}$

Analagous to the discrete case, we define

$$
f _ { X } ( x ) = \int _ { - \infty } ^ { \infty } f _ { X Y } ( x , y ) d y ,
$$

as the marginal probability density function (or marginal density) of X, and similarly for $f _ { Y } ( y )$

## 3.4 Conditional distributions

Conditional distributions seek to answer the question, what is the probability distribution over Y , when we know that X must take on a certain value x? In the discrete case, the conditional probability mass function of X given Y is simply

$$
p _ { Y | X } ( y | x ) = \frac { p _ { X Y } ( x , y ) } { p _ { X } ( x ) } ,
$$

assuming that $p _ { X } ( x ) \neq 0$

In the continuous case, the situation is technically a little more complicated because the probability that a continuous random variable X takes on a specific value x is equal to $\mathrm { z e r o } ^ { 4 }$ . Ignoring this technical point, we simply define, by analogy to the discrete case, the conditional probability density of Y given $X = x$ to be

$$
f _ { Y | X } ( y | x ) = \frac { f _ { X Y } ( x , y ) } { f _ { X } ( x ) } ,
$$

provided $f _ { X } ( x ) \neq 0 .$

## 3.5 Bayes’s rule

A useful formula that often arises when trying to derive expression for the conditional probability of one variable given another, is Bayes’s rule.

In the case of discrete random variables X and Y ,

$$
P _ { Y | X } ( y | x ) = \frac { P _ { X Y } ( x , y ) } { P _ { X } ( x ) } = \frac { P _ { X | Y } ( x | y ) P _ { Y } ( y ) } { \sum _ { y ^ { \prime } \in V a l ( Y ) } P _ { X | Y } ( x | y ^ { \prime } ) P _ { Y } ( y ^ { \prime } ) } .
$$

If the random variables X and Y are continuous,

$$
f _ { Y | X } ( y | x ) = \frac { f _ { X Y } ( x , y ) } { f _ { X } ( x ) } = \frac { f _ { X | Y } ( x | y ) f _ { Y } ( y ) } { \int _ { - \infty } ^ { \infty } f _ { X | Y } ( x | y ^ { \prime } ) f _ { Y } ( y ^ { \prime } ) d y ^ { \prime } } .
$$

## 3.6 Independence

Two random variables X and Y are independent if $F _ { X Y } ( x , y ) = F _ { X } ( x ) F _ { Y } ( y )$ for all values of x and y. Equivalently,

• For discrete random variables, $p _ { X Y } ( x , y ) \ = \ p _ { X } ( x ) p _ { Y } ( y )$ for all $x \ \in \ V a l ( X ) , \ y \ \in$ $V a l ( Y )$

• For discrete random variables, $p _ { Y | X } ( y | x ) = p _ { Y } ( y )$ whenever $p _ { X } ( x ) \ \neq \ 0$ for all $y \in$ $V a l ( Y )$

• For continuous random variables, $f _ { X Y } ( x , y ) = f _ { X } ( x ) f _ { Y } ( y )$ for all $x , y \in \mathbb { R }$

• For continuous random variables, $f _ { Y | X } ( y | x ) = f _ { Y } ( y )$ whenever $f _ { X } ( x ) \neq 0$ for all $y \in \mathbb R$

$$
F _ { Y | X } ( y , x ) = \operatorname* { l i m } _ { \Delta x \to 0 } P ( Y \leq y | x \leq X \leq x + \Delta x ) .
$$

It can be easily seen that if $F ( x , y )$ is differentiable in both x, y then,

$$
F _ { Y \mid X } ( y , x ) = \int _ { - \infty } ^ { y } \frac { f _ { X , Y } ( x , \alpha ) } { f _ { X } ( x ) } d \alpha
$$

and therefore we define the conditional PDF of Y given $X = x$ in the following way,

$$
f _ { Y | X } ( y | x ) = { \frac { f _ { X Y } ( x , y ) } { f _ { X } ( x ) } }
$$

Informally, two random variables X and Y are independent if “knowing” the value of one variable will never have any effect on the conditional probability distribution of the other variable, that is, you know all the information about the pair $( { \bar { X } } , Y )$ by just knowing $f ( x )$ and $f ( y )$ . The following lemma formalizes this observation:

Lemma 3.1. If X and Y are independent then for any subsets A, $B \subseteq \mathbb { R }$ , we have,

$$
P ( X \in A , Y \in B ) = P ( X \in A ) P ( Y \in B )
$$

By using the above lemma one can prove that if X is independent of $Y$ then any function of X is independent of any function of Y .

## 3.7 Expectation and covariance

Suppose that we have two discrete random variables $X , Y$ and $g : \mathbf { R } ^ { 2 } \longrightarrow \mathbf { R }$ is a function of these two random variables. Then the expected value of g is defined in the following way,

$$
E [ g ( X , Y ) ] \triangleq \sum _ { x \in V a l ( X ) } \sum _ { y \in V a l ( Y ) } g ( x , y ) p _ { X Y } ( x , y ) .
$$

For continuous random variables $X , Y$ , the analogous expression is

$$
E [ g ( X , Y ) ] = \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } g ( x , y ) f _ { X Y } ( x , y ) d x d y .
$$

We can use the concept of expectation to study the relationship of two random variables with each other. In particular, the covariance of two random variables X and Y is defined as

$$
\begin{array} { r l r } { C o v [ X , Y ] } & { { } \triangleq } & { E [ ( X - E [ X ] ) ( Y - E [ Y ] ) ] } \end{array}
$$

Using an argument similar to that for variance, we can rewrite this as,

$$
\begin{array} { r c l } { { C o v [ X , Y ] } } & { { = } } & { { E [ ( X - E [ X ] ) ( Y - E [ Y ] ) ] } } \\ { { } } & { { = } } & { { E [ X Y - X E [ Y ] - Y E [ X ] + E [ X ] E [ Y ] ] } } \\ { { } } & { { = } } & { { E [ X Y ] - E [ X ] E [ Y ] - E [ Y ] E [ X ] + E [ X ] E [ Y ] ] } } \\ { { } } & { { = } } & { { E [ X Y ] - E [ X ] E [ Y ] . } } \end{array}
$$

Here, the key step in showing the equality of the two forms of covariance is in the third equality, where we use the fact that $E [ X ]$ and $E [ Y ]$ are actually constants which can be pulled out of the expectation. When $C o v [ X , Y ] = 0$ , we say that X and $\check { Y }$ are uncorrelated5.

## Properties:

- (Linearity of expectation) $E [ f ( X , Y ) + g ( X , Y ) ] = E [ f ( X , Y ) ] + E [ g ( X , Y ) ] .$

- V ar[X + Y ] = V ar[X ] + V ar[Y ] + 2C ov[X, Y ].

- If X and Y are independent, then $C o v [ X , Y ] = 0 .$

- If X and Y are independent, then $E [ f ( X ) g ( Y ) ] = E [ f ( X ) ] E [ g ( Y ) ]$

## 4 Multiple random variables

The notions and ideas introduced in the previous section can be generalized to more than two random variables. In particular, suppose that we have n continuous random variables, $X _ { 1 } ( \omega ) , X _ { 2 } ( \omega ) , \dots X _ { n } ( \omega )$ . In this section, for simplicity of presentation, we focus only on the continuous case, but the generalization to discrete random variables works similarly.

## 4.1 Basic properties

We can define the joint distribution function of $X _ { 1 } , X _ { 2 } , \ldots , X _ { n } ,$ , the joint probability density function of $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ , the marginal probability density function of $X _ { 1 }$ , and the conditional probability density function of $X _ { 1 }$ given $X _ { 2 } , \ldots , X _ { n }$ , as

$$
\begin{array} { r c l } { F _ { X _ { 1 } , X _ { 2 } , \ldots , X _ { n } } ( x _ { 1 } , x _ { 2 } , \ldots x _ { n } ) } & { = } & { P ( X _ { 1 } \leq x _ { 1 } , X _ { 2 } \leq x _ { 2 } , \ldots , X _ { n } \leq x _ { n } ) } \\ { f _ { X _ { 1 } , X _ { 2 } , \ldots , X _ { n } } ( x _ { 1 } , x _ { 2 } , \ldots x _ { n } ) } & { = } & { \displaystyle \frac { \partial ^ { n } F _ { X _ { 1 } , X _ { 2 } , \ldots , X _ { n } } ( x _ { 1 } , x _ { 2 } , \ldots x _ { n } ) } { \partial x _ { 1 } \ldots \partial x _ { n } } } \\ { f _ { X _ { 1 } } ( X _ { 1 } ) } & { = } & { \displaystyle \int _ { - \infty } ^ { \infty } \cdots \int _ { - \infty } ^ { \infty } f _ { X _ { 1 } , X _ { 2 } , \ldots , X _ { n } } ( x _ { 1 } , x _ { 2 } , \ldots x _ { n } ) d x _ { 2 } \ldots d x _ { n } } \\ { f _ { X _ { 1 } | X _ { 2 } , \ldots , X _ { n } } ( x _ { 1 } | x _ { 2 } , \ldots x _ { n } ) } & { = } & { \displaystyle \frac { f _ { X _ { 1 } , X _ { 2 } , \ldots , X _ { n } } ( x _ { 1 } , x _ { 2 } , \ldots . x _ { n } ) } { f _ { X _ { 2 } , \ldots , X _ { n } } ( x _ { 1 } , x _ { 2 } , \ldots . x _ { n } ) } } \end{array}
$$

To calculate the probability of an event $A \subseteq \mathbb { R } ^ { n }$ we have,

$$
P ( ( x _ { 1 } , x _ { 2 } , . . . x _ { n } ) \in A ) = \int _ { ( x _ { 1 } , x _ { 2 } , . . . x _ { n } ) \in A } f _ { X _ { 1 } , X _ { 2 } , . . . , X _ { n } } ( x _ { 1 } , x _ { 2 } , . . . x _ { n } ) d x _ { 1 } d x _ { 2 } \dots d x _ { n }\tag{4}
$$

Chain rule: From the definition of conditional probabilities for multiple random variables, one can show that

$$
\begin{array} { r c l } { f ( x _ { 1 } , x _ { 2 } , \dots , x _ { n } ) } & { = } & { f ( x _ { n } | x _ { 1 } , x _ { 2 } \dots , x _ { n - 1 } ) f ( x _ { 1 } , x _ { 2 } \dots , x _ { n - 1 } ) } \\ & { = } & { f ( x _ { n } | x _ { 1 } , x _ { 2 } \dots , x _ { n - 1 } ) f ( x _ { n - 1 } | x _ { 1 } , x _ { 2 } \dots , x _ { n - 2 } ) f ( x _ { 1 } , x _ { 2 } \dots , x _ { n - 2 } ) } \\ & { = } & { \dots ~ = ~ f ( x _ { 1 } ) \displaystyle \prod _ { i = 2 } ^ { n } f ( x _ { i } | x _ { 1 } , \dots , x _ { i - 1 } ) . } \end{array}
$$

Independence: For multiple events, $A _ { 1 } , \ldots , A _ { k }$ , we say that $A _ { 1 } , \ldots , A _ { k }$ are mutually independent if for any subset $S \subseteq \{ 1 , 2 , \ldots , k \}$ , we have

$$
P ( \cap _ { i \in S } A _ { i } ) = \prod _ { i \in S } P ( A _ { i } ) .
$$

Likewise, we say that random variables $X _ { 1 } , \ldots , X _ { n }$ are independent if

$$
f ( x _ { 1 } , \dots , x _ { n } ) = f ( x _ { 1 } ) f ( x _ { 2 } ) \cdot \cdot \cdot f ( x _ { n } ) .
$$

Here, the definition of mutual independence is simply the natural generalization of independence of two random variables to multiple random variables.

Independent random variables arise often in machine learning algorithms where we assume that the training examples belonging to the training set represent independent samples from some unknown probability distribution. To make the significance of independence clear, consider a “bad” training set in which we first sample a single training example $( x ^ { ( 1 ) } , y ^ { ( 1 ) } )$ from the some unknown distribution, and then add $m - 1$ copies of the exact same training example to the training set. In this case, we have (with some abuse of notation)

$$
P ( ( x ^ { ( 1 ) } , y ^ { ( 1 ) } ) , \dots . . . ( x ^ { ( m ) } , y ^ { ( m ) } ) ) \neq \prod _ { i = 1 } ^ { m } P ( x ^ { ( i ) } , y ^ { ( i ) } ) .
$$

Despite the fact that the training set has size $m ,$ , the examples are not independent! While clearly the procedure described here is not a sensible method for building a training set for a machine learning algorithm, it turns out that in practice, non-independence of samples does come up often, and it has the effect of reducing the “effective size” of the training set.

## 4.2 Random vectors

Suppose that we have n random variables. When working with all these random variables together, we will often find it convenient to put them in a vector $X \bar { = } [ X _ { 1 } X _ { 2 } \dots X _ { n } ] ^ { T }$ . We call the resulting vector a random vector (more formally, a random vector is a mapping from $\Omega \operatorname { t o } \mathbb { R } ^ { n } )$ . It should be clear that random vectors are simply an alternative notation for dealing with n random variables, so the notions of joint PDF and CDF will apply to random vectors as well.

Expectation: Consider an arbitrary function from $g : \mathbb { R } ^ { n }  \mathbb { R }$ . The expected value of this function is defined as

$$
E [ g ( X ) ] = \int _ { \mathbb { R } ^ { n } } g ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } ) f _ { X _ { 1 } , X _ { 2 } , . . . , X _ { n } } ( x _ { 1 } , x _ { 2 } , . . . x _ { n } ) d x _ { 1 } d x _ { 2 } \dots d x _ { n } ,\tag{5}
$$

where $\scriptstyle \int _ { \mathbb { R } ^ { \eta } }$ n is n consecutive integrations from −∞ to ∞. If g is a function from $\mathbb { R } ^ { n }$ to $\mathbb { R } ^ { m }$ , then the expected value of $g$ is the element-wise expected values of the output vector, i.e., if $g$ is

$$
\begin{array} { r } { g ( x ) = \left[ \begin{array} { l } { g _ { 1 } ( x ) } \\ { g _ { 2 } ( x ) } \\ { \quad \vdots } \\ { g _ { m } ( x ) } \end{array} \right] , } \end{array}
$$

Then,

$$
E [ g ( X ) ] = \left[ \begin{array} { c } { E [ g _ { 1 } ( X ) ] } \\ { E [ g _ { 2 } ( X ) ] } \\ { \vdots } \\ { E [ g _ { m } ( X ) ] } \end{array} \right] .
$$

Covariance matrix: For a given random vector $X : \Omega \to \mathbb { R } ^ { n }$ , its covariance matrix Σ is the $n \times n$ square matrix whose entries are given by $\Sigma _ { i j } = C o v [ X _ { i } , X _ { j } ]$

From the definition of covariance, we have

$$
\begin{array} { r l } { \Sigma ~ = ~ } & { [ \begin{array} { c c c c } { C o v | X _ { 1 } , X _ { 1 } | } & { \cdots } & { C o v | X _ { 1 } , X _ { n } | } \\ { \vdots } & { \ddots } & { \vdots } \\ { C o v | \bar { X } _ { n } , X _ { 1 } | } & { \cdots } & { C o v | \bar { X } _ { n } , X _ { n } | } \end{array} ] } \\ { ~ } & { = ~ } & { [ \begin{array} { c c c c } { E [ X _ { 1 } ^ { 2 } | - E [ X _ { 1 } ] E [ X _ { 1 } ] } & { \cdots } & { E [ X _ { 1 } X _ { n } ] - E [ X _ { 1 } ] E [ X _ { n } ] } \\ { \vdots } & { \ddots } & { \ddots } \\ { E [ X _ { n } X _ { 1 } ] - E [ X _ { n } ] E [ X _ { 1 } ] } & { \cdots } & { E [ X _ { n } ^ { 2 } ] - E [ X _ { n } ] E [ X _ { n } ] } \end{array} ] } \\ { ~ } & { = ~ } & { [ \begin{array} { c c c c } { E [ X _ { 1 } ^ { 2 } ] } & { \cdots } & { E [ X _ { 1 } X _ { n } ] } \\ { \vdots } & { \ddots } & { \vdots } \\ { E [ X _ { n } X _ { 1 } ] } & { \cdots } & { E [ X _ { n } ^ { 2 } ] } \end{array} ] } \\ { ~ } & { = ~ } &  [ \begin{array} { c c c c } { \sum _ { i } ^ { ~ } \chi _ { 1 } ^ { ~ } \chi _ { 1 } } & { \cdots } & { \zeta } \\ { \vdots } & { \ddots } & { \vdots } \\ { E [ X _ { n } X _ { 1 } ] } & { \cdots } & { E [ X _ { n } ^ { 2 } ] } \end{array} ] - [ \begin{array} { c c c c } { E [ X _ { 1 } | E [ X _ { 1 } ] } & { \cdots } & { E [ X _ { 1 } | E [ X _ { n } ] } \\ { \vdots } & { \ddots } & { \vdots } \\ { E [ X _ { n } E [ X _ { 1 } ] } & { \cdots } &  E [ X \end{array} \end{array}
$$

where the matrix expectation is defined in the obvious way.

The covariance matrix has a number of useful properties:

$\Sigma \succeq 0 ;$ that is, Σ is positive semidefinite.

$\Sigma = \Sigma ^ { T }$ ; that is, Σ is symmetric.

## 4.3 The multivariate Gaussian distribution

One particularly important example of a probability distribution over random vectors X is called the multivariate Gaussian or multivariate normal distribution. A random vector $X \in \mathbb { R } ^ { n }$ is said to have a multivariate normal (or Gaussian) distribution with mean $\boldsymbol { \mu } \in \mathbb { R } ^ { n }$ and covariance matrix $\Sigma \in \mathbb { S } _ { + + } ^ { n }$ (where $\mathbb { S } _ { + + } ^ { n }$ refers to the space of symmetric positive definite $n \times n$ matrices)

$$
f _ { X _ { 1 } , X _ { 2 } , \ldots , X _ { n } } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ; \mu , \Sigma ) = { \frac { 1 } { ( 2 \pi ) ^ { n / 2 } | \Sigma | ^ { 1 / 2 } } } \exp \left( - { \frac { 1 } { 2 } } ( x - \mu ) ^ { T } \Sigma ^ { - 1 } ( x - \mu ) \right) .
$$

We write this as $X \sim { \mathcal { N } } ( \mu , \Sigma )$ . Notice that in the case $n = 1$ , this reduces the regular definition of a normal distribution with mean parameter $\mu _ { 1 }$ and variance $\Sigma _ { 1 1 }$

Generally speaking, Gaussian random variables are extremely useful in machine learning and statistics for two main reasons. First, they are extremely common when modeling “noise” in statistical algorithms. Quite often, noise can be considered to be the accumulation of a large number of small independent random perturbations affecting the measurement process; by the Central Limit Theorem, summations of independent random variables will tend to “look Gaussian.” Second, Gaussian random variables are convenient for many analytical manipulations, because many of the integrals involving Gaussian distributions that arise in practice have simple closed form solutions. We will encounter this later in the course.

## 5 Other resources

A good textbook on probablity at the level needed for CS229 is the book, A First Course on Probability by Sheldon Ross.