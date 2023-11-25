var o = "alert",
    r = "bs.alert",
    a = "." + r,
    h = {
        CLOSE: "close" + a,
        CLOSED: "closed" + a,
        CLICK_DATA_API: "click" + a + ".data-api"
    },
    f = "alert",
    d = "fade",
    m = "show",
    p = function () 
    {
        function i(t) { this._element = t }
        var t = i.prototype;
        return t.close = function (t) {
            var e = this._element;
            t && (e = this._getRootElement(t)),
                this._triggerCloseEvent(e)
                    .isDefaultPrevented() || this._removeElement(e)
        },
            t.dispose = function () {
                g.removeData(this._element, r),
                    this._element = null
            },
            t._getRootElement = function (t) {
                var e = _.getSelectorFromElement(t),
                    n = !1; return e && (n = document.querySelector(e)),
                        n || (n = g(t).closest("." + f)[0]), n
            },
            t._triggerCloseEvent = function (t) {
                var e = g.Event(h.CLOSE); return g(t).trigger(e), e
            },
            t._removeElement = function (e) {
                var n = this; if (g(e).removeClass(m), g(e).hasClass(d)) {
                    var t = _.getTransitionDurationFromElement(e);
                    g(e).one(_.TRANSITION_END, function (t) {
                        return n._destroyElement(e, t)
                    }).
                        emulateTransitionEnd(t)
                }
                else this._destroyElement(e)
            },
            t._destroyElement = function (t) {
                g(t).detach().trigger(h.CLOSED).remove()
            },
            i._jQueryInterface = function (n) {
                return this.each(function () {
                    var t = g(this),
                        e = t.data(r);
                    e || (e = new i(this),
                        t.data(r, e)),
                        "close" === n && e[n](this)
                })
            },

            g(document).on(h.CLICK_DATA_API, '[data-dismiss="alert"]',
                p._handleDismiss(new p)),
            g.fn[o] = p._jQueryInterface,
            g.fn[o].Constructor = p, g.fn[o]
                .noConflict = function () { return g.fn[o] = c, p._jQueryInterface };
    }