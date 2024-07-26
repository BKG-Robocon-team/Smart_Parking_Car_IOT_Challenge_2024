	<?php  
if (session_status() == PHP_SESSION_NONE) {
    session_start();
		if(isset($_SESSION['phone']))
			{
				
				
				} 
			else
			{
				//header("Location: index.php");
			}
}
 ?>
	
	<header>
		<div id="logo">
			<img src="src/logo.png" style="position:absolute;"/>
		</div>
		
		
		
		<nav>
			<ul>
				<li class="hor"><a href="index.php">Home</a></li>
			<!--	<li class="hor dropdown"><a href="streetlayout.php">Street Layout</a> </li>-->
			<li class="hor dropdown"><a href="zones.php">Bản đô bãi đỗ xe</a> </li>
			<li class="hor dropdown"><a href="contact.php">Contact Us</a></li>
				
			</ul>
		</nav>
	</header>
	
	<section id="hinges">
		<img src="src/h2.png">
		<img src="src/h2.png">
		<img src="src/h2.png">
		<img src="src/h2.png">
		<img src="src/h2.png">
		<img src="src/h2.png">
	</section>