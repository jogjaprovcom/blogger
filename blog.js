var

loader = new THREE.FileLoader( scope.manager );

loader.setPath(this.path ); loader.setResponseType( &#39;arraybuffer&#39; );

if (scope.crossOrigin === &#39;use-credentials&#39;) {

loader.setWithCredentials( true );

}

loader.load( url, function ( data ) {

try {

scope.parse(data, resourcePath, function (gltf) {

onLoad( gltf);

scope.manager.itemEnd(url);

}, _onError);

} catch (e) {

_onError( e );

}

}, onProgress, onError );

},

setDRACOLoader: function (dracoLoader) {

this.dracoLoader dracoLoader;

return this;

},
  THREE.GLTFLoader = ( function () {

function GLTFLoader (manager) {

THREE.Loader.call( this, manager );

this.dracoLoader = null;

this.ddsLoader = null;

GLTFLoader.prototype = Object.assign( Object.create( THREE.Loader.prototype ), {

constructor: GLTFLoader,

load: function (url, onLoad, onProgress, onError) {

var scope = this;

var resourcePath;

if (this.resourcePath !== * ) {

resourcePath = this.resourcePath;

} else if (this.path !== &#39;&#39;) {

resourcePath = this.path;

} else {

resourcePath = THREE.LoaderUtils.extractUrlBase( url);

}

// Tells the LoadingManager to track an extra item, which resolves after

// the model is fully loaded. This means the count of items loaded will

// be incorrect, but ensures manager.onLoad() does not fire early.

scope.manager.itemStart(url);

var _onError = function (e) {

if ( onError) {

onError( e );
  
