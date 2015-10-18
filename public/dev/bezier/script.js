var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var interval;

var p0 = {x:Math.floor(Math.random()*500), y:Math.floor(Math.random()*500)};
var p1 = {x:Math.floor(Math.random()*500), y:Math.floor(Math.random()*500)};
var p2 = {x:Math.floor(Math.random()*500), y:Math.floor(Math.random()*500)};
var p3 = {x:Math.floor(Math.random()*500), y:Math.floor(Math.random()*500)};

//3次ベジェ曲線
function bezierApp(runBool){
	var ball = {x:0, y:0, speed:.005, t:0};

	function initialScreen(){
		ctx.fillStyle = "#eee";
		ctx.fillRect(0, 0, canvas.width, canvas.height);

		ctx.strokeStyle = "#000";
		ctx.strokeRect(1, 1, canvas.width-2, canvas.height-2);

		// 点P0からP3の描画
		ctx.fillStyle = "rgba(255,0,0,0.6)";
		ctx.beginPath();
		ctx.arc(p0.x, p0.y, 10, 0, Math.PI*2, true);
		ctx.fill();

		ctx.fillStyle = "rgba(0,0,0,0.6)";
		ctx.beginPath();
		ctx.arc(p1.x, p1.y, 10, 0, Math.PI*2, true);
		ctx.fill();

		ctx.fillStyle = "rgba(0,0,0,0.6)";
		ctx.beginPath();
		ctx.arc(p2.x, p2.y, 10, 0, Math.PI*2, true);
		ctx.fill();

		ctx.fillStyle = "rgba(0,0,255,0.6)";
		ctx.beginPath();
		ctx.arc(p3.x, p3.y, 10, 0, Math.PI*2, true);
		ctx.fill();

		// 点P0からP3を結ぶ線の描画
		ctx.strokeStyle = "rgba(0,0,0,0.8)";
		ctx.beginPath();

		ctx.moveTo(p0.x, p0.y);
		ctx.lineTo(p1.x, p1.y);
		ctx.closePath();

		ctx.moveTo(p1.x, p1.y);
		ctx.lineTo(p2.x, p2.y);
		ctx.closePath();

		ctx.moveTo(p2.x, p2.y);
		ctx.lineTo(p3.x, p3.y);
		ctx.closePath();

		ctx.stroke();
	}

	function drawScreen(){

		var t = ball.t;

		var cx = 3*(p1.x-p0.x);
		var bx = 3*(p2.x-p1.x)-cx;
		var ax = p3.x - p0.x - cx - bx;

		var cy = 3*(p1.y-p0.y);
		var by = 3*(p2.y-p1.y)-cy;
		var ay = p3.y - p0.y - cy - by;

		var xt = ax*(t*t*t) + bx*(t*t) + cx*t + p0.x;
		var yt = ay*(t*t*t) + by*(t*t) + cy*t + p0.y;

		ball.t += ball.speed;
		if(ball.t>1){
			ball.t=1;
		}

		// ボールの描画
		ctx.fillStyle = "#42aac7";
		ctx.beginPath();
		ctx.arc(xt, yt, 3, 0, Math.PI*2, true);
		ctx.fill();
	}

	if(runBool) {
		interval = setInterval(drawScreen, 33);
	} else {
		initialScreen();
	}
}

window.onload = bezierApp(false);

// AngularJSのコントローラ
function pointsController($scope){
	$scope.p0 = {x:p0.x, y:p0.y};
	$scope.p1 = {x:p1.x, y:p1.y};
	$scope.p2 = {x:p2.x, y:p2.y};
	$scope.p3 = {x:p3.x, y:p3.y};

	$scope.replot = function(){
		if(interval){ clearInterval(interval); }

		$scope.p0.x=parseInt($scope.p0.x);
		$scope.p0.y=parseInt($scope.p0.y);
		$scope.p1.x=parseInt($scope.p1.x);
		$scope.p1.y=parseInt($scope.p1.y);
		$scope.p2.x=parseInt($scope.p2.x);
		$scope.p2.y=parseInt($scope.p2.y);
		$scope.p3.x=parseInt($scope.p3.x);
		$scope.p3.y=parseInt($scope.p3.y);

		p0 = {x:$scope.p0.x, y:$scope.p0.y};
		p1 = {x:$scope.p1.x, y:$scope.p1.y};
		p2 = {x:$scope.p2.x, y:$scope.p2.y};
		p3 = {x:$scope.p3.x, y:$scope.p3.y};

		bezierApp(false);
	}

	$scope.run = function(){
		if(interval){ clearInterval(interval); }
		bezierApp(true);
	}
}
