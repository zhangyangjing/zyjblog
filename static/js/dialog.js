(function() {
    function Dialog(innerHTML) {
        var dialogHtml = "<div style='top: -1px; left: -1px; display: flex; position: fixed; z-index: 9999; min-width: 80px; background-color: blanchedalmond; border-radius: 4px; box-shadow: 0px 0px 6px 0px gray; align-items: center; padding: 8px ;overflow: overlay;'>" + innerHTML + "</div>";
        var div = document.createElement('div');
        div.innerHTML = dialogHtml;
        this.dialogElement = div.firstChild;
    }

    Dialog.prototype = {
        update: function(innerHTML) {
            this.dialogElement.innerHTML = innerHTML;
            this.dialogs.resetPosition();
        },
        dimission: function() {
            this.dialogs.dimissionDialog(this);
        }
    }

    function Dialogs() {
        this.dialogArray = [];
        Dialog.prototype.dialogs = this;
        window.onresize = this.resetPosition.bind(this);
    }

    Dialogs.prototype = {
        showDialog: function(innerHTML, delay) {
            var dialog = new Dialog(innerHTML);
            document.body.appendChild(dialog.dialogElement);
            this.dialogArray.push(dialog);
            this.resetPosition();
            var _this = this;
            if (undefined != delay) {
                setTimeout(function() {
                    dialog.dimission();
                }, delay);
            }
            return dialog;
        },

        dimissionDialog: function(dialog) {
            this.dialogArray = this.dialogArray.filter(function(e) {return e != dialog});
            this.resetPosition();
            dialog.dialogElement.style.left = window.innerWidth + 'px';
            setTimeout(function() {
                dialog.dialogElement.remove();
            }, 500);
        }, 

        dimissionAllDialogs: function() {
            console.log('dimissionAllDialogs');     
        },

        resetPosition: function() {
            var verticalOffset = 0;
            var needReCall = false;
            for (var index in this.dialogArray) {
                var dialogElement = this.dialogArray[index].dialogElement;
                dialogElement.style.top = (window.innerHeight - dialogElement.offsetHeight - verticalOffset - 20) + "px";
                if (-1 == parseInt(dialogElement.style.left)) {
                    dialogElement.style.left = window.innerWidth + "px";
                    needReCall = true;
                } else {
                    dialogElement.style.transition = "all 0.3s linear";
                    dialogElement.style.left = (window.innerWidth - dialogElement.offsetWidth - 20) + "px";
                }
                verticalOffset += dialogElement.offsetHeight + 8;
            }
            if (needReCall) {
                requestAnimationFrame(this.resetPosition.bind(this));
            }
        }
    };

    window.dialogs = new Dialogs();
})();
