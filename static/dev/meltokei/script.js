var canvas, ctx;

window.onload = function(){
	canvas = document.getElementById("canvas");
	ctx = canvas.getContext("2d");

	function drawScreen(){
		ctx.save(); // 変換行列の初期状態（全く回転していない状態）を保存

		ctx.fillStyle = "#fdfae5";
		ctx.fillRect(0,0,400,400);

		drawCircles();
		drawFace();

		// 回転を含む処理の後には必ず変換行列を初期状態に戻し、再度保存しておく
		ctx.restore();
		ctx.save();

		// 長針
		var date = new Date();
		var angle = date.getMinutes() * 6;
		ctx.translate(200,200);
		ctx.rotate(angle*Math.PI/180);
		ctx.translate(-200,-200);

		ctx.fillStyle = "#ff9db1";
		fillRoundRect(200-4,75,8,125,3);

		ctx.restore();
		ctx.save();

		// 秒針
		angle = date.getSeconds() * 6;
		ctx.translate(200,200);
		ctx.rotate(angle*Math.PI/180);
		ctx.translate(-200,-200);

		ctx.strokeStyle = "#ff9db1";
		ctx.beginPath();
		ctx.moveTo(200,230);
		ctx.lineTo(200,75);
		ctx.stroke();

		ctx.restore();
		ctx.save();

		// 短針
		angle = date.getHours() * 30 + date.getMinutes()/10 * 5;
		ctx.translate(200,200);
		ctx.rotate(angle*Math.PI/180);
		ctx.translate(-200,-200);

		ctx.fillStyle = "#ff9db1";
		fillRoundRect(200-4,110,8,90,3);

		ctx.restore();

		ctx.fillStyle = "#ffbdcd";
		ctx.beginPath();
		ctx.arc(200,200,7,0,Math.PI*2,true);
		ctx.fill();
	}

	drawScreen();
	setInterval(drawScreen, 1000); //1秒おき
}

function fillRoundRect(l, t, w, h, r){
	var pi= Math.PI;
	ctx.beginPath();
	ctx.arc(l + r, t + r, r, - pi, - 0.5 * pi, false);
	ctx.arc(l + w - r, t + r, r, - 0.5 * pi, 0, false);
	ctx.arc(l + w - r, t + h - r, r, 0, 0.5 * pi, false);
	ctx.arc(l + r, t + h - r, r, 0.5 * pi, pi, false);
	ctx.closePath();
	ctx.fill();
}

function drawCircles(){
	ctx.fillStyle = "#ffed78";
	ctx.beginPath();
	ctx.arc(200,200,200,0,Math.PI*2,true);
	ctx.fill();

	ctx.fillStyle = "#cbbc75";
	ctx.beginPath();
	ctx.arc(200,200,185,0,Math.PI*2,true);
	ctx.fill();

	ctx.fillStyle = "#ffe1e7";
	ctx.beginPath();
	ctx.arc(200,200,175,0,Math.PI*2,true);
	ctx.fill();

	ctx.fillStyle = "#ffedf3";
	ctx.beginPath();
	ctx.arc(200,200,130,0,Math.PI*2,true);
	ctx.fill();

	ctx.fillStyle = "#fffae4";
	ctx.beginPath();
	ctx.arc(200,200,75,0,Math.PI*2,true);
	ctx.fill();

	ctx.fillStyle = "#ffd9e5";
	ctx.beginPath();
	ctx.arc(200,200,70,0,Math.PI*2,true);
	ctx.fill();

	ctx.fillStyle = "#fffae4";
	ctx.beginPath();
	ctx.arc(200,200,60,0,Math.PI*2,true);
	ctx.fill();
}

function drawFace(){
	// てっぺんの紫から時計まわりに色を設定
	var colors = new Array("#dd5aeb","#ff5e89","#ff5756","#ff7e48","#f0a931","#ead025","#b0d833","#64c941","#23be8c","#3cb8d4","#648bd4","#967ddd");
	for(var i=0; i<12; i++){
		ctx.fillStyle = colors[i];
		ctx.beginPath();
		ctx.moveTo(200, 30);
		ctx.lineTo(200+8, 30+10);
		ctx.lineTo(200+8, 30+10+18); // (ここ+y方向へ3)が右斜め下の六角形のてっぺん
		ctx.lineTo(200, 30+10+18+10);
		ctx.lineTo(200-8, 30+10+18);
		ctx.lineTo(200-8, 30+10);
		ctx.lineTo(200, 30);
		ctx.closePath();
		ctx.fill();

		ctx.beginPath();
		ctx.moveTo(208, 61);
		ctx.lineTo(208+8, 61+10);
		ctx.lineTo(208+8, 61+10+18);
		ctx.lineTo(208, 61+10+18+10);
		ctx.lineTo(208-8, 61+10+18);
		ctx.lineTo(208-8, 61+10);
		ctx.lineTo(208, 61);
		ctx.closePath();
		ctx.fill();

		ctx.translate(200,200);
		ctx.rotate(30*Math.PI/180);
		ctx.translate(-200,-200);
	}
}
