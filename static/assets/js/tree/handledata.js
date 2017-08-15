function getLevelById(data,id) {
	return getParents(data,id).length;
}

function hasChilds(data,id){
	return getChildById(data,id).length !== 0;
}

function getChildById(arr,pid){
	var newArr = [];
	for( var i = 0; i < arr.length; i++ ){
		if( arr[i].pid == pid ){
			newArr.push(arr[i]);
		}
	};

	return newArr;
}

function getParents(data,currentId){
	var arr = [];
	for( var i = 0; i < data.length; i++ ){
		if( data[i].id == currentId ){
			arr.push(data[i]);
			arr = arr.concat(getParents(data,data[i].pid))
			break;
		}
	}
	return arr;
}