function numController($scope){
	$scope.binary_pattern = /^[01]+$/;
	$scope.decimal_pattern = /^[0-9]+$/;
	$scope.hex_pattern = /^[0-9A-Fa-f]+$/;

	$scope.binary = function(){
		if($scope.num.binary && parseInt($scope.num.binary,2) < 9007199254740992){
			$scope.num.decimal = parseInt($scope.num.binary,2);
			$scope.num.hex = parseInt($scope.num.binary,2).toString(16);
		} else {
			$scope.num.decimal = undefined;
			$scope.num.hex = undefined;
		}
	}

	$scope.decimal = function(){
		if($scope.num.decimal && parseInt($scope.num.decimal) < 9007199254740992){
			$scope.num.binary = parseInt($scope.num.decimal).toString(2);
			$scope.num.hex = parseInt($scope.num.decimal).toString(16);
		} else {
			$scope.num.binary = undefined;
			$scope.num.hex = undefined;
		}
	}

	$scope.hex = function(){
		if($scope.num.hex && parseInt($scope.num.hex,16) < 9007199254740992){
			$scope.num.binary = parseInt($scope.num.hex,16).toString(2);
			$scope.num.decimal = parseInt($scope.num.hex,16);
		} else {
			$scope.num.binary = undefined;
			$scope.num.decimal = undefined;
		}
	}
}

