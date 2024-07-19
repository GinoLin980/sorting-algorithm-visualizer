import sys; sys.dont_write_bytecode = True
import customtkinter as ctk


class Sort_Visualizer_GUI(ctk.CTk):
    def __init__(self, settings: dict[str, str|int]):
        super().__init__()
        self.title("Sorting Visualizer")
        self.geometry("360x185")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.running = True
        self.grid_rowconfigure(0, weight=0)
        self.settings = settings

        self.reso = ctk.StringVar(value="720p")
        self.orient = ctk.StringVar(value="Landscape")
        self.elements = ctk.IntVar(value=512)
        self.algo = ctk.StringVar(value="Quick Sort")

        label1 = ctk.CTkLabel(self, text="Please Choose the Options and Hit GO", font=ctk.CTkFont(size=18))
        reso_label = ctk.CTkLabel(self, text="Resolution:", font=ctk.CTkFont(size=14))
        reso_option = ctk.CTkOptionMenu(self, values=["480p", "720p", "1080p", "1440p", "2560p"], variable=self.reso, command=lambda x: self.reso.set(x))
        orient_label = ctk.CTkLabel(self, text="Orientation:", font=ctk.CTkFont(size=14))
        orient_option = ctk.CTkOptionMenu(self, values=["Portrait", "Landscape"], variable=self.orient, command=lambda x: self.orient.set(x))
        elements_label = ctk.CTkLabel(self, text="Elements:", font=ctk.CTkFont(size=14))
        elements_option = ctk.CTkOptionMenu(self, values=["10", "50", "100", "256", "512", "1024", "2048"], variable=self.elements, command=lambda x: self.elements.set(x))
        algo_label = ctk.CTkLabel(self, text="Algorithm:", font=ctk.CTkFont(size=14))
        algo_option = ctk.CTkOptionMenu(self,values=["Bubble Sort", "Quick Sort"], variable=self.algo, command=lambda x: self.algo.set(x))
        go_button = ctk.CTkButton(self, text="GO", fg_color="lime green", text_color="black", font=ctk.CTkFont(size=13, weight="bold"), command=self.GO_callback)

        label1.grid(row=0, column=0, sticky="ew", columnspan=2)
        reso_label.grid(row=1, column=0, padx=25, sticky="w")
        orient_label.grid(row=1, column=1, padx=25, sticky="w")
        reso_option.grid(row=2, column=0, padx=20, sticky="w")
        orient_option.grid(row=2, column=1, padx=20, sticky="w")
        elements_label.grid(row=3, column=0, padx=25, sticky="w")
        algo_label.grid(row=3, column=1, padx=25, sticky="w")
        elements_option.grid(row=4, column=0, padx=20, sticky="w")
        algo_option.grid(row=4, column=1, padx=20, sticky="w")
        go_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def GO_callback(self):
        self.settings = {"reso": int(self.reso.get()[:-1]), "orient": self.orient.get(), "elements": self.elements.get(), "algo": self.algo.get(), "Start_Visual": True}

    def get_settings(self):
        return self.settings

    def on_closing(self):
        self.running = False
        self.quit()
        self.destroy()

    def run(self):
        if self.running:
            self.update()
        else:
            sys.exit()


if __name__ == "__main__":
    settings = {}
    APP = Sort_Visualizer_GUI(settings)
    while True:
        APP.run()